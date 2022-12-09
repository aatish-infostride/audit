from django.urls import path
from dashboard import views

urlpatterns = [
    path('home/',views.dashboard,name= "home" ),
    path('profile/',views.profile,name= "profile" ),
    path('change-password/',views.change_password,name= "change-password" ),
]