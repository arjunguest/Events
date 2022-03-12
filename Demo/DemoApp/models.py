from django.db import models

# Create your models here.

class Categories(models.Model):
    category=models.CharField(max_length=100)
    def __str__(self):
        return self.category
    
class Events(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    location=models.CharField(max_length=100)
    start_date=models.DateTimeField(blank=True,null=True)
    end_date=models.DateTimeField(null=True)
    image=models.ImageField(upload_to='uploaded_picture',blank=True,null=True)
    categories=models.ForeignKey(Categories,on_delete=models.CASCADE, null=True)
    published=models.BooleanField(default=False)
    paid=models.BooleanField(default=False)
        
        
    def __str__(self):
        return self.title