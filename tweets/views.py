import random
from django.conf import settings
from this import d
from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .forms import TweetForm
from .models import Tweet
from .serializers import TweetSerializer

# Create your views here.

ALLOWED_HOSTS = settings.ALL_HOSTS


def home_view(request, *args, **kwargs):
    # r eturn HttpResponse("<h1> hello world </h1>")
    return render(request, "pages/home.html", contenxt={}, status=200)


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.object.all()
    tweets_list = [{"id": x.id, "content": x.content,
                    "likes": random.randint(0, 100)} for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)


def tweet_create_view(request, *args, **kwargs):
    serializer = TweetSerializer(data=request.POST or None)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return JsonResponse(serializer.data, status=201)
    return JsonResponse({}, status=400)


def tweet_create_view_pure_django(request, *args, **kwargs):
    user = request.user
    if not request.user.is_authenticated:
        if request.is_ajax():
            return JsonResponse({}, status=401)
        return redirect(settings.LOGIN_URL)

    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_Valid():
        obj = form.save(commit=False)
        obj.user = request.user or None
        obj.save()

        if request.is_ajax():
            # 201 == created Items
            return JsonResponse(obj.serialize(), status=201)

        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)
    return render(request, 'components/form.html', context={"form": form})


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    Consume by JS or Swift/Java/Android
    """
    data = {
        "id": tweet_id,
        # "image"
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404

    return JsonResponse(data, status=status)
