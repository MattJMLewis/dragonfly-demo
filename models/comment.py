from dragonfly import models
from dragonfly.utils import Utils


class Comment(models.Model):

    comment = models.TextField()
    article_id = models.IntField(unsigned=True)
    user_id = models.IntField(unsigned=True)

    class Meta:
        comment_article_fk = models.ForeignKey('article_id').references('id').on('articles')
        comment_user_fk = models.ForeignKey('user_id').references('id').on('users')

    def user(self):
        return models.BelongsTo(target='user').delayed_init(self._database_values, self.meta)

    def article(self):
        return models.BelongsTo(target='article').delayed_init(self._database_values, self.meta)

    def url(self):
        return Utils.url(f"comments/{self.id}")