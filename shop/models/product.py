from email.mime import image
from email.policy import default
from django.db import models
from .category import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1) 
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='uploads/products')

    def __str__(self):
        return self.name


    @staticmethod
    def get_all_products():
        return Product.objects.all()
