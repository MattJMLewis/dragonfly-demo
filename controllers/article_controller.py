from dragonfly import Auth
from dragonfly import view, RedirectResponse, request, ErrorResponse
from models.article import Article


class ArticleController:

    def index(self):
        articles = Article().paginate(size=5)
        return view('articles.index', articles=articles[0], pagination=articles[1])

    def show(self, id):
        return view('articles.show', article=Article().find(id), user=Auth.user())

    def create(self):
        return view('articles.create')

    def store(self, request_data):
        request_data['user_id'] = Auth.user().id
        article = Article().create(request_data)
        return RedirectResponse(article.url())

    def edit(self, id):
        article = Article().find(id)

        if article.user().id == Auth.user().id:
            return view('articles.edit', article=article)

        return ErrorResponse('Unauthorised', 500)

    def update(self, id, request_data):
        article = Article().find(id)

        if Auth.user().id == article.user_id:
            article.update(request_data)

        return RedirectResponse(article.url())

    def delete(self, id):
        article = Article().find(id)

        if article.user().id == Auth.user().id:
            article.delete()

        return RedirectResponse(request.base_uri + '/articles')

    def add_cookie(self):

        response = RedirectResponse(request.base_uri + '/articles')
        response.header('Set-cookie', 'session_id=testing')

        return response
