from dragonfly import Controller
from dragonfly import View
from dragonfly import RedirectResponse
from models.article import Article
from dragonfly.utils import url


class ArticleController(Controller):

    def index(self):
        return View("articles.index", articles=Article().all()).make()

    def show(self, id):
        return View("articles.show", article=Article().find(id)).make()

    def create(self):
        return View("articles.create").make()

    def edit(self, id):
        return View("articles.edit", article=Article().find(id)).make()

    def store(self, request_data):
        article = Article().create(request_data)
        return RedirectResponse(article.url())

    def update(self, id, request_data):
        article = Article().find(id).update(request_data)
        return RedirectResponse(article.url())

    def destroy(self, id):
        Article().find(id).delete()
        return RedirectResponse(url('articles'))
