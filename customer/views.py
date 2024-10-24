from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
import json
from django.contrib.auth.decorators import login_required   
from .models import Customer
@login_required
def customer_view(request):
    customers = Customer.objects.all() 
    context = {'customers': customers}
    return render(request, 'customer/customer.html', context)
  
def add_customer(request):

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            customer_name = data.get('customerName')    
            customer_email = data.get('customerEmail')
            customer_mobile = data.get('customerMobile')
            new_customer = Customer(name=customer_name, email=customer_email, phone=customer_mobile)
            new_customer.save()
            return HttpResponse('Customer added successfully')
        except Exception as e:
             return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'customer/customer.html')

def delete_customer(request,cutomer_id):
    customer = Customer.objects.get(id=cutomer_id)
    customer.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
   
def edit_customer(request,cutomer_id):
    customer = Customer.objects.get(id=cutomer_id)
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            customer.name = data.get('customerName')    
            customer.email = data.get('customerEmail')
            customer.mobile = data.get('customerMobile')
            customer.save()
            return JsonResponse({'message': 'Customer updated successfully!'}, status=200)
        except Exception as e:
             return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'name': customer.name, 'email': customer.email, 'phone': customer.phone})