from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categories(models.Model):
    category=models.CharField(max_length=100)
    def __str__(self):
        return self.category
    
class Events(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    location=models.CharField(max_length=100)
    start_date=models.DateField(blank=True,null=True)
    end_date=models.DateField(null=True)
    image=models.ImageField(upload_to='uploaded_picture',blank=True,null=True)
    categories=models.ForeignKey(Categories,on_delete=models.CASCADE, null=True)
    published=models.BooleanField(default=False)
    paid=models.BooleanField(default=False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
        
        
    def __str__(self):
        return self.title