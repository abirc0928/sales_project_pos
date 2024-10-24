from django.db import models
from category.models import Category
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    unit = models.CharField(max_length=10)
    image = models.ImageField(upload_to='products/')

    category = models.ForeignKey(Category, on_delete=models.CASCADE)