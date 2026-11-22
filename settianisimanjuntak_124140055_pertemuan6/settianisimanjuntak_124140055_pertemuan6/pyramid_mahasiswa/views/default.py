from pyramid.view import notfound_view_config, view_config


@view_config(route_name='home', renderer='json')
def home(request):
    """Halaman utama: ringkasan endpoint API yang tersedia."""
    return {
        'aplikasi': 'Pyramid RESTful API Mahasiswa & Matakuliah',
        'endpoints': {
            'mahasiswa': '/api/mahasiswa',
            'matakuliah': '/api/matakuliah',
        },
    }


@notfound_view_config(renderer='json')
def notfound_view(request):
    """Handler 404 untuk URL/method yang tidak cocok dengan route manapun."""
    request.response.status = 404
    return {'error': 'Resource tidak ditemukan'}
