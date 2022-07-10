from django.forms import ModelForm

from .models import User, Post


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = "user", "title", "body"


class UserCreateForm(ModelForm):
    class Meta:
        model = User
        fields = "name", "username", "email"
