from pyramid.config import Configurator


def main(global_config, **settings):
    """Entry point aplikasi WSGI Pyramid."""
    with Configurator(settings=settings) as config:
        config.include('pyramid_tm')       # transaksi otomatis per request
        config.include('pyramid_retry')    # retry jika terjadi konflik transaksi
        config.include('.models')          # engine, session, request.dbsession
        config.include('.routes')          # URL dispatch
        config.scan('.views')              # daftarkan semua @view_config
    return config.make_wsgi_app()
