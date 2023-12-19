from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1= request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'authentication/register.html')
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken')
                return render(request, 'authentication/register.html')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already in use')
                    return render(request, 'authentication/register.html')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    messages.success(request, 'Account created successfully')
                    return render(request, 'authentication/login.html')
    return render(request, 'authentication/register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        auth = authenticate(request, username=username, password=password)
        if auth is not None:
            login(request, auth)
            return redirect('dashboard/')
        else:
            messages.error(request, 'Invalid Credentials, Try Again!')
            return render(request, 'authentication/login.html')
    else:
        return render(request, 'authentication/login.html')
@login_required(login_url='login')    
def logout_user(request):
    logout(request) 
    return render(request, 'authentication/logout.html')