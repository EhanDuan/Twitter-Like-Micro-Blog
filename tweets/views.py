
from django.conf import settings

from django.shortcuts import render


# Create your views here.

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1> hello world </h1>")
    return render(request, "pages/feed.html")


def tweets_list_view(request, *args, **kwargs):
    return render(request, "tweets/list.html")


def tweets_detail_view(request, tweet_id, *args, **kwargs):
    # r eturn HttpResponse("<h1> hello world </h1>")
    return render(request, "tweets/detail.html", context={"tweet_id": tweet_id})


def tweets_profile_view(request, username, *args, **kwargs):
    return render(request, "tweets/profile.html", context={"profile_username": username})
