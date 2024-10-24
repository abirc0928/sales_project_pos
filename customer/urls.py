from django.urls import path
from .views import customer_view,add_customer, delete_customer, edit_customer
urlpatterns = [
    path('',customer_view, name='customer_view' ),
    path('add/',add_customer, name='add_customer'),
    path('delete/<int:cutomer_id>/',delete_customer, name='delete_customer'),
    path('edit/<int:cutomer_id>/',edit_customer, name='edit_customer'),
]