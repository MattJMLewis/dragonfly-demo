import os

from config import NO_AUTH
from dragonfly.auth import Auth
from dragonfly.constants import DATA_METHODS
from dragonfly.request import request
from dragonfly.response import ErrorResponse


class CsrfMiddleware:
    actions = '*'

    def before(self):
        # Determine if csrf_token for form request is valid
        if request.method in DATA_METHODS and request.path not in NO_AUTH:
            try:
                token = request.get_data()['csrf_token']
            except KeyError:
                return ErrorResponse('No CSRF token', 500)

            if token != Auth.get('csrf_token'):
                return ErrorResponse('CSRF invalid', 500)

        # Set a csrf_token for the form request
        elif request.path not in NO_AUTH:
            Auth.set('csrf_token', os.urandom(25).hex())

    def after(self):
        pass
