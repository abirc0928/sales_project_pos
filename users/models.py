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