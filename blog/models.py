from django.db import models
from django.contrib.auth.models import User

# Create your models here.
   
class Tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name
    
class Image(models.Model):
    image = models.ImageField(upload_to="uploads/blog/images/", blank=True, null=True)


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_photo = models.ImageField( upload_to="uploads/blog/cover photos/", height_field=None, width_field=None, max_length=None)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, null=True)
    image = models.ManyToManyField('Image', blank=True)
    blog = models.TextField(null= True, blank =True)
    tags = models.ManyToManyField(Tags, blank=True)
    is_featured = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def approved_comments(self):
        return self.comments.filter(approve_comment = True)

    def __str__(self) -> str:
        return self.title



class Comment(models.Model):
    name = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30)
    blog = models.ForeignKey(Blog,related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(max_length=250)
    is_approved =  models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

