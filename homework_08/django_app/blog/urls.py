from django.urls import path

from .views import view_blog, PostCreateView, UserCreateView

app_name = "blog"

urlpatterns = [
    path("", view_blog, name="view_blog"),
    path("post/", PostCreateView.as_view(), name="add_post"),
    path("user/", UserCreateView.as_view(), name="add_user"),
]
