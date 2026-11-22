# Pyramid RESTful API: Manajemen Mahasiswa & Matakuliah

## Identitas Praktikan
- **Nama Lengkap** : Settiani Simanjuntak
- **NIM**          : 124140055
- **Kelas**        : RA

## Deskripsi Aplikasi
Aplikasi RESTful API berbasis **Pyramid Framework**, **SQLAlchemy ORM**, **Alembic**,
dan **PostgreSQL**. Aplikasi menyediakan operasi CRUD untuk dua resource:

| Resource   | Endpoint                | Keterangan                        |
|------------|-------------------------|-----------------------------------|
| Mahasiswa  | `/api/mahasiswa`        | Data mahasiswa (praktikum)        |
| Matakuliah | `/api/matakuliah`       | Data mata kuliah (tugas)          |

### Endpoint Matakuliah
| Method | URL                       | Fungsi                                  | Status           |
|--------|---------------------------|-----------------------------------------|------------------|
| GET    | `/api/matakuliah`         | Daftar seluruh mata kuliah              | 200              |
| GET    | `/api/matakuliah/{id}`    | Detail mata kuliah                      | 200 / 404        |
| POST   | `/api/matakuliah`         | Tambah mata kuliah                      | 200 / 400        |
| PUT    | `/api/matakuliah/{id}`    | Ubah mata kuliah                        | 200 / 400 / 404  |
| DELETE | `/api/matakuliah/{id}`    | Hapus mata kuliah                       | 200 / 404        |

Validasi: `kode_mk`, `nama_mk`, `sks`, `semester` wajib diisi; `sks` dan `semester`
harus bilangan bulat > 0; `kode_mk` harus unik.

## Instalasi & Menjalankan

### 1. Persiapan lingkungan
```bash
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate.bat
pip install --upgrade pip setuptools
pip install psycopg2-binary
pip install -e ".[testing]"
```

### 2. Siapkan database PostgreSQL
```sql
CREATE DATABASE pyramid_mahasiswa;
CREATE USER pyramid_user WITH ENCRYPTED PASSWORD 'pyramid_pass';
GRANT ALL PRIVILEGES ON DATABASE pyramid_mahasiswa TO pyramid_user;
\c pyramid_mahasiswa
GRANT ALL ON SCHEMA public TO pyramid_user;
```
Pastikan di `development.ini`:
```
sqlalchemy.url = postgresql://pyramid_user:pyramid_pass@localhost:5432/pyramid_mahasiswa
```

### 3. Migrasi database
```bash
alembic -c development.ini upgrade head
```

### 4. Seeding data awal
```bash
python -m pyramid_mahasiswa.scripts.initialize_db development.ini
```

### 5. Jalankan server
```bash
pserve development.ini --reload
```
Server berjalan di http://localhost:6543

## Pengujian (cURL)
```bash
curl http://localhost:6543/api/matakuliah
curl http://localhost:6543/api/matakuliah/1
curl -X POST http://localhost:6543/api/matakuliah -H "Content-Type: application/json" \
  -d '{"kode_mk":"IF4010","nama_mk":"Keamanan Informasi","sks":3,"semester":7}'
curl -X PUT http://localhost:6543/api/matakuliah/1 -H "Content-Type: application/json" \
  -d '{"nama_mk":"Pemrograman Web Lanjut","sks":4}'
curl -X DELETE http://localhost:6543/api/matakuliah/4
curl http://localhost:6543/api/matakuliah/999
```
Alternatif: gunakan file `api_test.http` dengan ekstensi *REST Client* di VS Code.

## Bukti Pengujian (Screenshot)
> Tempel screenshot hasil cURL/Postman untuk **semua endpoint** (Mahasiswa & Matakuliah).

### Mahasiswa
- GET all: `![](screenshots/mhs_get_all.png)`![alt text](image.png)
- GET one: `![](screenshots/mhs_get_one.png)`![alt text](image-1.png)
- POST: `![](screenshots/mhs_post.png)`![alt text](image-2.png)
- PUT: `![](screenshots/mhs_put.png)`![alt text](image-3.png)
- DELETE: `![](screenshots/mhs_delete.png)`![alt text](image-4.png)

### Matakuliah
- GET all: `![](screenshots/mk_get_all.png)`![alt text](image-5.png)
- GET one: `![](screenshots/mk_get_one.png)`![alt text](image-6.png)
- POST: `![](screenshots/mk_post.png)`![alt text](image-7.png)
- POST (400): `![](screenshots/mk_post_400.png)`![alt text](image-8.png)
- PUT: `![](screenshots/mk_put.png)`![alt text](image-9.png)
- DELETE: `![](screenshots/mk_delete.png)`![alt text](image-10.png)
- GET (404): `![](screenshots/mk_get_404.png)`![alt text](image-11.png)
