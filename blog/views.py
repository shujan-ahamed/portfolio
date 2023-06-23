from django.shortcuts import render
from blog.forms import Blog_Form

from blog.models import Blog, Tags, Comment
from portfolio.models import Resume
from django.utils.text import slugify
from  django.contrib import messages


# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    form = Blog_Form()

    if request.method == 'POST':
        print('posting')
        form = Blog_Form(request.POST, request.FILES)
        print('oj')
        if form.is_valid():
            title = form.cleaned_data['title']
            blog = form.save(commit=False)
            blog.user = request.user
            blog.slug = slugify(title)
            blog.save()
            print('ok')
            messages.success(request, "Submitted.")


        else:
            messages.error(request, "Invailed form.")
            print(form.errors, form.errors)
    
    context = {
        'blogs' : blogs,
        'form' : form,
    }
    return render(request, 'blog.html', context)

def blog_details(request, slug, tags=None):
    blog = Blog.objects.get(slug=slug)
    tags = blog.tags.all()
    resume = Resume.objects.get()
    comments = Comment.objects.all().order_by('-created_date')

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('text')

        comment = Comment(
            name = name,
            email = email,
            text = text,
            blog = blog,
        )
        comment.save()


    context = {
        'blog' : blog,
        'tags' :tags,
        'resume' : resume,
        'comments' : comments,
    }
    return render(request, 'blog_details.html', context)
