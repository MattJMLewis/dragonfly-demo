from routes import routes
from dragonfly import request
from wsgiref.simple_server import make_server
from dragonfly import Response
import sys

def app(environ, start_response):

    request.update_environ(environ)
    response = routes.dispatch_route()

    start_response(response.status, response.headers)
    return [response.content]

httpd = make_server('localhost', 8080, app)
httpd.serve_forever()
