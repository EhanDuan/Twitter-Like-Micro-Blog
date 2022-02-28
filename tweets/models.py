from django.db import models
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class Tweet(models.Model):
    # Maps to SQL data
    # id = models.AutoField(primary_key = True)
    # many users can have many tweets
    # 转发
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    # 如果A转发了B的帖子，B账户注销了，那么这里B的全部帖子都会删除，且A以往转发B的帖子也会失效
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    likes = models.ManyToManyField(
        User, related_name='tweet_user', blank=True, through=TweetLike)
    image = models.FileField(upload_to='image/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    @property
    def is_retweet(self):
        return self.parent != None

    def serialize(self):
        """
        old way to serialize
        """
        return {
            "id": self.id,
            "content": self.content,
            "likes": 0
        }
