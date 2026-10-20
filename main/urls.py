from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CineBoard.urls')),  # <--- Добавьте эту строчку, чтобы CineBoard открывался на главной
    path('cineboard/', include('CineBoard.urls')),
    path('shop/', include('myShop.urls')),
    path('tour/', include('tour.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)