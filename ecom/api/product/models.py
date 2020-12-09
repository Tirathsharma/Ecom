from django.db import models
from api.category.models import category
# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=50)
    description =models.CharField( max_length=250)
    price= models.CharField( max_length=50)
    stock= models.CharField( max_length=50)
    is_active=models.BooleanField( default=True,blank=True)
    image=models.ImageField(upload_to='image/' ,blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    category=models.ForeignKey(category, on_delete=models.SET_NULL,blank=True, null=True)
    def __str__(self):
        return self.name