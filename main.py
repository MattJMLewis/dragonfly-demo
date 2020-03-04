from wsgiref.simple_server import make_server

from config import URL
from dragonfly import request
from routes import routes


def app(environ, start_response):
    request.update_environ(environ)
    response = routes.dispatch_route()

    start_response(response.status, response.headers)
    return [response.content]


url = URL[7:]
host, port = url.split(':')

httpd = make_server(host, int(port), app)
httpd.serve_forever()
