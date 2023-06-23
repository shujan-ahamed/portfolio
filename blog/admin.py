from django.contrib import admin

from blog.models import Blog, Image, Tags, Comment

# Register your models here.
admin.site.register(Blog)
admin.site.register(Image)
admin.site.register(Tags)
admin.site.register(Comment)