from django.urls import path,include
from .views import signup_views
urlpatterns = [
   path('signup/', signup_views, name='signup_views')
]
