from django.urls import path

from .views import produect_view, add_product,delete_product, edit_product
urlpatterns = [
    path("", produect_view, name="produect"),
    path("add/", add_product, name="add_product"),
    path("delete/<int:product_id>/", delete_product, name="delete_product"),
    path('edit/<int:product_id>/', edit_product, name='edit_product')
]