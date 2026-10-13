from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myShop.urls')),
    path('', include('tour.urls')),
    
]
