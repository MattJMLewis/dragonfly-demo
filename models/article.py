from config import URL
from dragonfly import models


class Article(models.Model):
    name = models.VarCharField(length=255)
    text = models.TextField()
    user_id = models.IntField(unsigned=True)

    class Meta:
        article_user_fk = models.ForeignKey('user_id').references('id').on('users')

    def url(self):
        return f"{URL}/articles/{self.id}"

    def comments(self):
        return self.add_relationship(models.HasMany(target='comment'))

    def user(self):
        return self.add_relationship(models.BelongsTo(target='user'))
