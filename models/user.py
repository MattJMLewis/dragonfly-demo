from dragonfly.db import models
from dragonfly.utils import Utils


class User(models.Model):
    username = models.VarCharField(null=False)
    email = models.VarCharField(length=50)
    password = models.VarCharField(length=128)
    salt = models.VarCharField(length=32)
    session_id = models.VarCharField(length=64, null=True)

    def url(self):
        return Utils.url(f"users/{self.id}")

    def articles(self):
        return self.add_relationship(models.HasMany(target='article'))

    def comments(self):
        return self.add_relationship(models.HasMany(target='comment'))