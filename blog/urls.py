from django.urls import path

from .views import  blog, blog_details

urlpatterns = [
    path('', blog, name='blog'),
    path('blog_details/<slug:slug>/', blog_details, name='blog_details'),
]