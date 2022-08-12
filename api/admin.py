from django.contrib import admin

from api.models import Post, Comment, Friendship

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Friendship)
