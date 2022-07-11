from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, null=False, unique=False)
    username = models.CharField(max_length=32, null=False, unique=True)
    email = models.CharField(max_length=50, null=False, unique=True)
    biography = models.TextField(max_length=300, null=True, blank=True, unique=False)

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=100, null=False, unique=True)
    body = models.TextField(max_length=500, null=False, blank=True, unique=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.title
