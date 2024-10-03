from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginFrom(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter username'}))

class OtpForm(forms.Form):
    otp_verify = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'placeholder': 'Enter OTP'}))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('mobile_number', 'address', 'website')
        widget = {
            'mobile_number': forms.TextInput(attrs={'placeholder': 'Enter mobile number'}),
            'address': forms.Textarea(attrs={'placeholder': 'Enter address', 'rows': 3}),
            'website': forms.TextInput(attrs={'placeholder': 'Enter website'}),
        }

    