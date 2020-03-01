import hashlib
import os

from dragonfly import view, RedirectResponse, Auth
from dragonfly.utils import Utils
from models.user import User


class UserController:

    def login(self):
        return view('users.login')

    def register(self):
        return view('users.register')

    def store(self, request_data):

        del request_data['password_confirmation']

        salt = os.urandom(16)
        request_data['salt'] = salt.hex()
        request_data['password'] = hashlib.pbkdf2_hmac('sha256', request_data['password'].encode('utf-8'), salt, 100000,
                                                       dklen=64).hex()

        user = User().create(request_data)
        user.session_id = os.urandom(32).hex()
        user.save()

        response = RedirectResponse(Utils.url('articles'))
        response.header('Set-cookie', f"session_id={user.session_id}; SameSite=Strict;")

        return response

    def show(self, id):

        return view('users.show', user=User().find(id))

    def authenticate(self, request_data):
        user = User().where('username', '=', request_data['username']).first()

        if user:
            to_check = hashlib.pbkdf2_hmac('sha256', request_data['password'].encode('utf-8'), bytes.fromhex(user.salt),
                                           100000, dklen=64).hex()

            if to_check == user.password:
                user.session_id = os.urandom(32).hex()
                user.save()

                response = RedirectResponse(Utils.url('articles'))
                response.header('Set-cookie', f"session_id={user.session_id}; SameSite=Strict;")

                return response

        return RedirectResponse(Utils.url('login'))

    def deauthenticate(self, request_data):
        user = Auth.user()

        user.session_id = ''
        user.save()

        response = RedirectResponse(Utils.url('login'))
        response.header('Set-cockie', "session_id=''; SameSite=Strict;")

        return response
