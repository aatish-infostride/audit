from importlib.resources import contents
from web.models import Users
from django.db import models

# Create your models here.



class Blogs(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE) # many to one relationship
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    status = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta :
        db_table = 'blogs'


class Attributes(models.Model):
    blog = models.OneToOneField(Blogs,on_delete=models.CASCADE) #one to one realationship
    content = models.CharField(max_length=100)
    meta_title = models.CharField(max_length=50)
    

class Categories(models.Model):
   
    title = models.CharField(max_length=50)
    meta_title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

  #n  

class InCategories(models.Model):
    blog =  models.OneToOneField(Blogs,on_delete=models.CASCADE)
    categories  = models.ForeignKey(Categories, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comments(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Likes(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    likes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




 