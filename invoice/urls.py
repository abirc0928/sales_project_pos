from django.urls import path
from .views import invoice_view

urlpatterns = [
    path('', invoice_view, name='invoice_view'),
]