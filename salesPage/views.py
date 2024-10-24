from django.shortcuts import render
from django.contrib.auth.decorators import login_required   

@login_required
# Create your views here.
def salesPage(request):
    return render(request, 'salesPage/salesPage.html')