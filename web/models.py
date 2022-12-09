
from django.db import models


# Create your models here.

class CommonInfo(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
    

#users model:

class Users(CommonInfo):

    email = models.TextField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middel_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)    
    profile_image = models.ImageField()
    last_logged_in =  models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'users'
    
# user details model:

class User_Details(CommonInfo):
    
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    about = models.TextField()
    is_email_verified = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
# Roles model:
    
class Roles(CommonInfo):
    
   
    tittle = models.TextField(max_length=255)
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

# user_roles model:

class User_Roles(CommonInfo):
    
    user = models.OneToOneField(Users,on_delete=models.CASCADE)
    roles = models.ForeignKey(Roles,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    

    

    
    
    
    
    
    
