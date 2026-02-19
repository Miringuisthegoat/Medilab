
from django.contrib import admin
from django.urls import path,include
from healthapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('healthapp.urls')),
]
