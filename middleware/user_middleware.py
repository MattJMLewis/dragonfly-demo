from config import NO_AUTH
from dragonfly.request import request
from dragonfly.response import RedirectResponse
from dragonfly.utils import Utils
from models.user import User


class UserMiddleware:
    actions = "*"

    def before(self):

        if request.path not in NO_AUTH:
            try:
                session_id = request.cookies['session_id']
                user = User().where('session_id', '=', session_id).first()
                if not user:
                    return RedirectResponse(Utils.url('login'))

            except KeyError:
                return RedirectResponse(Utils.url('login'))

    def after(self):
        pass
