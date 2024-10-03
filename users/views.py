from django.shortcuts import render, redirect
from .forms import LoginFrom, OtpForm, ProfileForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required   
from django.contrib.auth import authenticate, login, logout
from .models import UserOTP, Profile
import random
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = LoginFrom(request.POST, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            otp = ''.join([str(random.randint(0,9)) for i in range(6)])
            user_otp, created = UserOTP.objects.get_or_create(user=user)
            user_otp.otp = otp
            user_otp.save()
            print("user id: ", user.id)
            request.session['otp_user_id'] = user.id
            return redirect('otp-verify') 
        #     login(request,user)
        #     return redirect('home')
        # else:
        #     return HttpResponse('Invalid username or password')
        
           
    else:
        form = LoginFrom()
    context = {
        'form': form
    }
    return render(request, 'login.html',context)

def otp_verify_view(request):
    user_id = request.session['otp_user_id']
    if not user_id:
        return redirect('login')
    
    user = User.objects.get(id=user_id)
    user_otp = UserOTP.objects.get(user=user)
    if request.method == 'POST':
        form = OtpForm(request.POST)
        
        if form.is_valid():
            otp = form.cleaned_data.get('otp_verify')
            print(otp, user_otp.otp)
            if otp == user_otp.otp:
                del request.session['otp_user_id']
                user_otp.delete()
                login(request,user)
                return redirect('home')
            else:
                form.add_error('otp_verify', 'Invalid OTP')
    else:
        form = OtpForm()
    
    context = {
        'form': form
    }
    return render(request, 'opt_verify.html', context)

@login_required
def home_view(request): 
    return render(request, 'home.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def update_profile_view(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
         profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=profile)

    context={
        'form': form
    }
    return render(request, 'profile_update.html', context)