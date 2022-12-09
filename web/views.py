from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.

APP_THEME = ''

def login(request):
    return render(request, '_templates/'+APP_THEME+'pages/web/auth/login.html')

def signup(request):
    return render(request, '_templates/'+APP_THEME+'pages/web/auth/signup.html')

def forgot_password(request):
    return render(request, '_templates/'+APP_THEME+'pages/web/auth/forgot-password.html')

def reset_password(request):
    return render(request, '_templates/'+APP_THEME+'pages/web/auth/reset-password.html')