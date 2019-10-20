from dragonfly import models
from dragonfly.utils import url


class Article(models.Model):

    id = models.IntField(null=False, primary_key=True, unsigned=True, auto_increment=True)
    name = models.CharField(null=False, unique=True, max_length=100)
    text = models.TextField()

    def url(self):
        return url(f"articles/{self.id}")

