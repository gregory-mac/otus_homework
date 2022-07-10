from django.urls import path

from .views import (
    view_blog,
    PostCreateView,
    UserCreateView,
    UserListView,
    UserDetailView
)

app_name = "blog"

urlpatterns = [
    path("", view_blog, name="view_blog"),
    path("post/", PostCreateView.as_view(), name="add_post"),
    path("user/", UserCreateView.as_view(), name="add_user"),
    path("ulist/", UserListView.as_view(), name="user_list"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
]
