from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    mobile_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)

    def __str__(self):  
        return f"Profile for user {self.user.username}"
    
class UserOTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6, blank=True, null=True) 
   
    
    def __str__(self):
        return f"OTP for user {self.user.username}"
    
# class Customer(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone = models.CharField(max_length=15)

# class Category(models.Model):
#     title = models.CharField(max_length=100)

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.FloatField()
#     unit = models.CharField(max_length=10)
#     image = models.ImageField(upload_to='products/')

#     category = models.ForeignKey(Category, on_delete=models.CASCADE)

# class Invoice(models.Model):
#     total = models.FloatField()
#     vat =  models.FloatField()
#     discount = models.FloatField()
#     payable = models.FloatField()

#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

# class Order(models.Model):
#     quantity = models.IntegerField()
#     total = models.FloatField()
    
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)