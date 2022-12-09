from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, '_templates/layouts/dashboard/dashboard.html' )

def profile(request):
    return render(request, '_templates/pages/dashboard/profile.html' )


def change_password(request):
    return render(request, '_templates/pages/dashboard/change-password.html')