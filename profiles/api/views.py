

from rest_framework import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from ..models import Profile
from django.conf import settings

User = get_user_model()
ALLOWED_HOSTS = settings.ALLOWED_HOSTS


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_follow_view(request, username, *args, **kwargs):
    me = request.user
    other_user_qs = User.objects.filter(username=username)
    if me.username == username:
        my_followers = me.profile.followers.all()
        return Response({"count": my_followers.count()}, status=200)

    if not other_user_qs.exists():
        return Response({}, status=404)

    other = other_user_qs.first()
    profile = other.profile
    data = request.data or {}
    action = data.get("action")
    if action == "unfollow":
        profile.followers.remove(me)
    elif action == "follow":
        profile.followers.add(me)
    else:
        pass

    current_followers_qs = profile.followers.all()
    return Response({"count": current_followers_qs.count()}, status=200)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def user_follow_view(request, username, *args, **kwargs):
#     current_user = request.user
#     to_follow_user =
#     return Response({}, status=400)
