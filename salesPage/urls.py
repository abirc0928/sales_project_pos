from django.urls import path

from .views import salesPage

urlpatterns = [
    path("", salesPage, name="salesPage"),
]