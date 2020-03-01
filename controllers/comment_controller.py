from dragonfly import Auth, RedirectResponse, Utils
from models.comment import Comment


class CommentController:

    def store(self, id, request_data):
        request_data['article_id'] = id
        request_data['user_id'] = Auth.user().id

        Comment().create(request_data)

        return RedirectResponse(Utils.url(f"articles/{id}"))

    def destroy(self, id):
        comment = Comment().find(id)

        if comment.user().id == Auth.user().id:
            comment.delete()

        return RedirectResponse((comment.article().url()))
