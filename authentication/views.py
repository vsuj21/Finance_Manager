from django.shortcuts import render
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# Create your views here.

class RegisterView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        auth = authenticate(request, username=username, password=password)
        if auth is not None:
            login(request, auth)
            return render(request, 'dashboard/index.html')
        else:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'authentication/login.html')
    else:
        return render(request, 'authentication/login.html')