from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username , password = password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Successfully loged in.')
            return redirect('dashboard')
        else:
            messages.error(request, "Invailed login credential!")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, "Successfully loged out.")
    return redirect('login')


def registration(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.error(request, 'This username is already taken, please try again.')
                return redirect('registration')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request, "This email is already taken, please try again.")
                    return redirect('registration')
                else:
                    user = User.objects.create(first_name = first_name, last_name = last_name, username= username, email= email, password = password)
                    user.save()
                    messages.success(request, 'Registration successful.')
                    return redirect('login')
        else:
            messages.error(request, "password don't matches")
            return redirect('ragistration')    

    else:
        return render(request, 'accounts/registration.html')



