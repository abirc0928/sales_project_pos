from django.shortcuts import render, get_object_or_404
from category.models import Category
from produect.models import Product
from django.http import JsonResponse, HttpResponseRedirect
import json
# Create your views here.
def produect_view(request):
    categories = Category.objects.all()
    products = Product.objects.all().order_by('-id') 
    
    # Correct the context dictionary
    context = {
        'categories': categories,
        'products': products
    }

    return render(request, 'produect/produect.html', context)

def add_product(request):
   
    if request.method == 'POST':
        
        name = request.POST.get('name')
        price = request.POST.get('price')
        unit = request.POST.get('unit')
        category_id = request.POST.get('category')
        image = request.FILES.get('image')

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Category not found'})

        product = Product.objects.create(
            name=name,
            price=price,
            unit=unit,
            image=image,
            category=category
        )

        return JsonResponse({'success': True})
    # Rendr form for GET request
    categories = Category.objects.all()
    return render(request, 'product_add.html', {'categories': categories})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)  
    product.delete() 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # Redirect back to the referring page

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'GET':
        data = {
            'category': product.category.id,
            'name': product.name,
            'price': product.price,
            'unit': product.unit,
            'image_url': product.image.url,
            'image_path': product.image.path
        }
        return JsonResponse(data)

    elif request.method == 'POST':
        category_id = request.POST.get('category')
        name = request.POST.get('name')
        price = request.POST.get('price')
        unit = request.POST.get('unit')
        image = request.FILES.get('image')

        product.category = Category.objects.get(id=category_id)
        product.name = name
        product.price = price
        product.unit = unit
        if image:
            product.image = image  

        product.save()  
        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})