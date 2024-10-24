from django.shortcuts import render
from django.contrib.auth.decorators import login_required   
 

@login_required
# Create your views here.
def invoice_view(request):
    return render(request, 'invoice/invoice.html')