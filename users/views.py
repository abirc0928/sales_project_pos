from django.shortcuts import render, redirect
from .forms import LoginFrom, OtpForm, ProfileForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required   
from django.contrib.auth import authenticate, login, logout
from .models import UserOTP, Profile
import random
from django.contrib.auth.models import User


def userLogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            # login(request, user)
            otp = ''.join([str(random.randint(0,9)) for i in range(6)])
            user_otp, created = UserOTP.objects.get_or_create(user=user)
            user_otp.otp = otp
            user_otp.save()
            print("user id: ", user.id)
            request.session['otp_user_id'] = user.id
            print(user)
            return redirect('userOTP')  
        else:
           
            return render(request, 'userLogin.html', {'error': 'Invalid credentials'})

    return render(request, 'userLogin.html')
    

def userOTP(request):
    user_id = request.session.get('otp_user_id') 
    if not user_id:
        return redirect('login')  

    user = User.objects.get(id=user_id)  
    user_otp = UserOTP.objects.get(user=user)  

    if request.method == 'POST':
        otp = request.POST.get('otp_verify')  
        if otp:
            if otp == user_otp.otp:
                del request.session['otp_user_id']  
                user_otp.delete()  
                login(request, user)  
                return redirect('dashboard')  
            else:

                error_message = "Invalid OTP. Please try again."
                return render(request, 'sendOtp.html', {'error_message': error_message})

    return render(request, 'sendOtp.html')  


@login_required
def logout_view(request):
    logout(request)
    return redirect('index')

# @login_required
# def update_profile_view(request):
#     try:
#         profile = request.user.profile
#     except Profile.DoesNotExist:
#          profile = Profile.objects.create(user=request.user)

#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = ProfileForm(instance=profile)

#     context={
#         'form': form
#     }
#     return render(request, 'profile_update.html', context)