from .views import profile_detail_api_view
from django.urls import path

urlpatterns = [
    path('<str:username>/', profile_detail_api_view),
    path('<str:username>/follow', profile_detail_api_view),


]
