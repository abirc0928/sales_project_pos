from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required   
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Category
@login_required
# Create your views here.
def create_category(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            category_name = data.get('name')
            
            new_category = Category(name=category_name)
            new_category.save()
            return render(request, 'category/category.html')
          
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request, 'category/category.html', context)
    

def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)  # Safely get the category
    category.delete()  # Delete the category
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # Redirect back to the referring page

def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            category.name = data.get('name')
            category.save()
            return JsonResponse({'message': 'Category updated successfully!'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    # For GET request, return category details as JSON to populate the form
    return JsonResponse({'name': category.name})