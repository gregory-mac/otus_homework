from django.contrib import admin

from .models import User, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "title_short")
    list_display_links = ("title_short", )

    def title_short(self, obj: Post):
        if len(obj.title) < 20:
            return obj.title
        return obj.title[:20] + "..."


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "username", "email")
    list_display_links = ("username", )
