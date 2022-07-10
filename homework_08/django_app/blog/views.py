from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView

from .models import User, Post
from .forms import PostCreateForm, UserCreateForm


def view_blog(request: HttpRequest):
    posts = Post.objects.order_by("id").all()
    context = {
        "posts": posts,
    }
    return render(request, "blog/view_blog.html", context=context)


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm

    def get_success_url(self):
        return reverse("blog:view_blog")


class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm

    def get_success_url(self):
        return reverse("blog:view_blog")


class UserListView(ListView):
    model = User
    context_object_name = "users"
