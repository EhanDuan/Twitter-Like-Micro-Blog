from django.db import models
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Tweet(models.Model):
    # Maps to SQL data
    # id = models.AutoField(primary_key = True)
    # many users can have many tweets

    # 如果A转发了B的帖子，B账户注销了，那么这里B的全部帖子都会删除，且A以往转发B的帖子也会失效
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='image/', blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": 0
        }
