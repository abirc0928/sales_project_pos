
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
def index(request):
    return render(request, 'index.html')    

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('accounts/', include('signup.urls')),
    path('customer/', include('customer.urls')),
    path('category/', include('category.urls')),
    path('produect/', include('produect.urls')),
    path('sales/', include('salesPage.urls')),
    path('invoice/', include('invoice.urls')),
    path('report/', include('report.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
