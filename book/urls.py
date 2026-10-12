from django.urls import path
from . import views

urlpatterns = [
    path('hello_world/', views.hello_world_view),
    path('my_favourite_emodji/', views.my_favourite_emodji_view),
    path('about_my_self/', views.about_my_self_view),
    path('book/', views.book_list_view, name = 'book_list'),
    path('book/<int:book_id>', views.book_detail_view, name = 'book_detail'),
]