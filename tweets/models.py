from django.db import models
from django.conf import settings
from django.db import models
from django.db.models import Q

User = settings.AUTH_USER_MODEL


class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class TweetQuerySet(models.QuerySet):
    def by_username(self, username):
        return self.filter(user__username__iexact=username)

    def feed(self, user):
        profiles_exist = user.following.exists()
        followed_users_id = []

        if profiles_exist:
            followed_users_id = user.following.values_list(
                "user_id", flat=True)  # [x.user.id for x in profiles]

        # followed_users_id.append(user.id)
        return self.filter(
            Q(user__id__in=followed_users_id) |
            Q(user=user)
        ).distinct().order_by("-timestamp")


class TweetManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return TweetQuerySet(self.model, using=self._db)

    def feed(self, user):
        return self.get_queryset().feed(user)


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

    objects = TweetManager()

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
