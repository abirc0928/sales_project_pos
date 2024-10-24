from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render
from .views import dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),
]
