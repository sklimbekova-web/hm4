from django.urls import path 
from . import views

urlpatterns = [
    path('tour_list/', views.tour_list_view, name='tour_list_view'),
    path('tour/<int:pk>/', views.tour_detail_view, name='tour_detail_view'),
]