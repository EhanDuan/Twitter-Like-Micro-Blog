from .models import Profile
from cgi import test
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from .models import Tweet

User = get_user_model()


User = get_user_model()


class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="cfe", password="somepassword")
        self.userb = User.objects.create_user(
            username="cfe-2", password="somepassword")

    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='somepassword')
        return client

    def test_profile_created_via_signal(self):
        qs = Profile.objects.all()
        self.assertEqual(qs.count(), 2)

    def test_follow_api_endpoint(self):
        client = self.get_client()
        response = client.post(f"/api/tweets/{self.userb.username}/follow",
                               {
                                   "action": "follow"
                               }
                               )

        r_data = response.json()
        count = r_data.get("count")
        self.assertEqual(count, 1)

    def test_unfollow_api_endpoint(self):
        first = self.user
        second = self.userb
        first.profile.followers.add(second)

        client = self.get_client()
        response = client.post(f"/api/tweets/{self.userb.username}/follow",
                               {
                                   "action": "unfollow"
                               }
                               )

        r_data = response.json()
        count = r_data.get("count")
        self.assertEqual(count, 0)

    def test_following(self):
        first = self.user
        second = self.userb

        # added a follower
        first.profile.followers.add(second)

        # from a user, check other user is being followed
        second_user_following_whom = second.following.all()
        qs = second_user_following_whom.filter(user=first)
        # check new user has not followers
        first_user_following_no_one = first.following.add()

        self.assertTrue(qs.exists())
        self.assertFalse(first_user_following_no_one.exists())

    def test_cannot_follow_api_endpoint(self):
        client = self.get_client()
        response = client.post(f"/api/tweets/{self.user.username}/follow",
                               {
                                   "action": "follow"
                               }
                               )

        r_data = response.json()
        count = r_data.get("count")
        self.assertEqual(count, 0)
