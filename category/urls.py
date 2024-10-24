from django.urls import path
from .views import create_category,delete_category, edit_category

urlpatterns = [
    path('', create_category , name='category' ),
    path('delete/<int:category_id>/', delete_category, name='delete_category'),
    path('edit/<int:category_id>/', edit_category, name='edit_category'),
]
