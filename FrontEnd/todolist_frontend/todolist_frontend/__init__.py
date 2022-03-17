from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
my_session_factory = SignedCookieSessionFactory('itsaseekreet',cookie_name='sessionmae')

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_jinja2')
        config.include('pyramid_flash_message')
        config.include('.routes')
        config.set_session_factory(my_session_factory)
        config.scan()
    return config.make_wsgi_app()
