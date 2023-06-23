from django.db import models

# Create your models here.
class Portfolio(models.Model):
    type = models.CharField(max_length=50)
    image = models.ImageField(upload_to='portfolio/images/', null = True)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=350)
    url = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type

class Resume(models.Model):
    name = models.CharField( max_length=50)
    fb_link = models.CharField( max_length=50, blank=True)
    twitter_link = models.CharField( max_length=50, blank=True)
    linkedin_link = models.CharField( max_length=50, blank=True)
    github_link = models.CharField( max_length=50, blank=True)
    wp_link = models.CharField( max_length=50, blank=True)
    image = models.ImageField(upload_to='resume/images/', null = True)
    description = models.TextField(max_length=350)
    email = models.CharField( max_length=50)
    phone = models.CharField( max_length=50)
    profile_title = models.CharField( max_length=50)
    profile_description = models.CharField( max_length=50)
    adress = models.CharField( max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    from_date = models.DateField(auto_now_add=False)
    to_date = models.DateField(auto_now_add=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Education(models.Model):
    title = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    from_date = models.DateField(auto_now_add=False)
    to_date = models.DateField(auto_now_add=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Skills(models.Model):
    title = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class ContactMessages(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Achivements(models.Model):
    client = models.PositiveBigIntegerField()
    projects = models.PositiveBigIntegerField()
    coffee = models.PositiveBigIntegerField()

class Languages(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class Web_cat(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class Features(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title