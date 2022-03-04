"""tweetme2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include


from tweets.views import local_tweets_list_view, local_tweets_detail_view, local_tweets_profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tweets/', include('tweets.urls')),
    path('', local_tweets_list_view),
    path('<int:tweet_id>', local_tweets_detail_view),
    path('profile/<str:usename>', local_tweets_profile_view),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)