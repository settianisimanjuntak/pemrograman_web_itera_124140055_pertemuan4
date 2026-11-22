from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPNotFound,
    HTTPBadRequest,
)
from ..models import Matakuliah

REQUIRED_FIELDS = ('kode_mk', 'nama_mk', 'sks', 'semester')
TEXT_FIELDS = ('kode_mk', 'nama_mk')
INT_FIELDS = ('sks', 'semester')


def _bad_request(message):
    return HTTPBadRequest(json_body={'error': message})


def _not_found(matakuliah_id):
    return HTTPNotFound(
        json_body={'error': f'Matakuliah dengan ID {matakuliah_id} tidak ditemukan'}
    )


def _validate_payload(data, partial=False):
    """Validasi payload JSON.

    partial=False -> dipakai POST (semua field wajib ada).
    partial=True  -> dipakai PUT (hanya field yang dikirim yang divalidasi).

    Return: (data_bersih, pesan_error). Salah satunya selalu None.
    """
    if not isinstance(data, dict):
        return None, 'Payload harus berupa objek JSON'

    if not partial:
        for field in REQUIRED_FIELDS:
            value = data.get(field)
            if value is None or (isinstance(value, str) and not value.strip()):
                return None, f'Field {field} wajib diisi!'

    clean = {}

    for field in TEXT_FIELDS:
        if field in data:
            value = data[field]
            if not isinstance(value, str) or not value.strip():
                return None, f'Field {field} harus berupa teks yang tidak kosong'
            clean[field] = value.strip()

    for field in INT_FIELDS:
        if field in data:
            value = data[field]
            # bool adalah subclass int di Python, jadi harus ditolak eksplisit
            if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
                return None, f'Field {field} harus berupa bilangan bulat positif (lebih dari 0)'
            clean[field] = value

    return clean, None


def _kode_exists(dbsession, kode_mk, exclude_id=None):
    query = dbsession.query(Matakuliah).filter(Matakuliah.kode_mk == kode_mk)
    if exclude_id is not None:
        query = query.filter(Matakuliah.id != exclude_id)
    return query.first() is not None


# 1. READ ALL
@view_config(route_name='matakuliah_list', renderer='json')
def matakuliah_list(request):
    """Menampilkan seluruh daftar mata kuliah"""
    items = request.dbsession.query(Matakuliah).order_by(Matakuliah.id.asc()).all()
    return {'matakuliahs': [m.to_dict() for m in items]}


# 2. READ ONE
@view_config(route_name='matakuliah_detail', renderer='json')
def matakuliah_detail(request):
    """Menampilkan detail mata kuliah berdasarkan ID (404 jika tidak ada)"""
    matakuliah_id = int(request.matchdict['id'])
    matakuliah = request.dbsession.query(Matakuliah).filter_by(id=matakuliah_id).first()

    if matakuliah is None:
        return _not_found(matakuliah_id)

    return {'matakuliah': matakuliah.to_dict()}


# 3. CREATE
@view_config(route_name='matakuliah_add', request_method='POST', renderer='json')
def matakuliah_add(request):
    """Menambahkan mata kuliah baru (400 jika data tidak lengkap/tidak valid)"""
    try:
        json_data = request.json_body
    except ValueError:
        return _bad_request('Body request harus berupa JSON yang valid')

    clean, error = _validate_payload(json_data, partial=False)
    if error:
        return _bad_request(error)

    dbsession = request.dbsession
    if _kode_exists(dbsession, clean['kode_mk']):
        return _bad_request(f"Kode MK {clean['kode_mk']} sudah terdaftar")

    matakuliah = Matakuliah(**clean)
    dbsession.add(matakuliah)
    dbsession.flush()  # eksekusi INSERT agar id dari PostgreSQL terisi

    return {'success': True, 'matakuliah': matakuliah.to_dict()}


# 4. UPDATE
@view_config(route_name='matakuliah_update', request_method='PUT', renderer='json')
def matakuliah_update(request):
    """Memperbarui data mata kuliah berdasarkan ID"""
    dbsession = request.dbsession
    matakuliah_id = int(request.matchdict['id'])

    matakuliah = dbsession.query(Matakuliah).filter_by(id=matakuliah_id).first()
    if matakuliah is None:
        return _not_found(matakuliah_id)

    try:
        json_data = request.json_body
    except ValueError:
        return _bad_request('Body request harus berupa JSON yang valid')

    clean, error = _validate_payload(json_data, partial=True)
    if error:
        return _bad_request(error)

    if 'kode_mk' in clean and _kode_exists(dbsession, clean['kode_mk'], exclude_id=matakuliah_id):
        return _bad_request(f"Kode MK {clean['kode_mk']} sudah terdaftar")

    for field, value in clean.items():
        setattr(matakuliah, field, value)

    return {'success': True, 'matakuliah': matakuliah.to_dict()}


# 5. DELETE
@view_config(route_name='matakuliah_delete', request_method='DELETE', renderer='json')
def matakuliah_delete(request):
    """Menghapus mata kuliah berdasarkan ID"""
    dbsession = request.dbsession
    matakuliah_id = int(request.matchdict['id'])

    matakuliah = dbsession.query(Matakuliah).filter_by(id=matakuliah_id).first()
    if matakuliah is None:
        return _not_found(matakuliah_id)

    dbsession.delete(matakuliah)

    return {'success': True, 'message': f'Matakuliah dengan ID {matakuliah_id} berhasil dihapus'}
