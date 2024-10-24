from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserRegistrationForm
from django.http import HttpResponse
# Create your views here.
def signup_views(request):
    print('1')
    if request.method == 'POST':
        print('3')
        form = CustomUserRegistrationForm(request.POST)
        print('4')
        if form.is_valid():
            print('5')
            form.save()
            print('6')
            messages.success(request, 'Registration successful! You can now log in.')
            print('7')
            return HttpResponse('signup_views')  # Redirect to login page or dashboard
        else:
            print('8')
            messages.error(request, 'There was an error with your registration. Please try again.')
    else:
        print('2')
        form = CustomUserRegistrationForm()
    
    context = {
        'form': form
    }
    return render(request, 'signup/signup.html', context)