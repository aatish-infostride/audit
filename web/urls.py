from django.contrib import admin
from django.urls import path , re_path

from web import views

urlpatterns = [
    path('auth/login', views.login,name="login"),
    path('auth/signup', views.signup,name="signup"),
    path('auth/forgot-password', views.forgot_password, name="forgot-password"),
    path('auth/reset-password', views.reset_password, name="reset-password"),
]