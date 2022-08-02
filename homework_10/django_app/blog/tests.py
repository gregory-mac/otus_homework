from django.test import TestCase
from django.urls import reverse
from .models import User, Post


class ViewTests(TestCase):
    fixtures = [
        "users.fixture.json",
        "posts.fixture.json",
    ]

    def test_user_list(self):
        response = self.client.get(
            reverse("blog:user_list"),
        )
        self.assertEqual(response.status_code, 200)

        users = User.objects.all()
        users_in_context = response.context["users"]
        self.assertEqual(len(users), len(users_in_context))

    def test_post_list(self):
        response = self.client.get(
            reverse("blog:view_blog"),
        )
        self.assertEqual(response.status_code, 200)

        posts = Post.objects.all()
        posts_in_context = response.context["posts"]
        self.assertEqual(len(posts), len(posts_in_context))


class AddViewTests(TestCase):
    fixtures = [
        "users.fixture.json",
    ]

    def test_get_add_user(self):
        response = self.client.get(
            reverse("blog:add_user"),
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>Add user</h1>", html=True)

    def test_get_add_post(self):
        response = self.client.get(
            reverse("blog:add_post"),
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>Add post</h1>", html=True)

    def test_add_user(self):
        post_data = {
            "name": "Jeremy",
            "username": "jeremy",
            "email": "jeremy@example.com"
        }
        response = self.client.post(
            reverse("blog:add_user"),
            data=post_data,
        )

        self.assertEqual(response.status_code, 302)

    def test_add_post(self):
        user = User.objects.get(username="john")
        post_data = {
            "user": user.id,
            "title": "Test title",
            "body": "Lorem ipsum dolor sit amet."
        }
        response = self.client.post(
            reverse("blog:add_post"),
            data=post_data,
        )

        self.assertEqual(response.status_code, 302)
