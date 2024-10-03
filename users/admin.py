from django.contrib import admin
from .models import Profile, UserOTP
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    

class UserOTPAdmin(admin.StackedInline):
    model = UserOTP
    can_delete = False
    verbose_name_plural = 'UserOTP'
class UserAdmin(BaseUserAdmin):
    # inlines = [ProfileInline, UserOTPAdmin]
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)