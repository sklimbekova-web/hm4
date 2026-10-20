from django.urls import path
from . import views

urlpatterns = [
    path('hello_world/', views.hello_world_view),
    path('my_favourite_emodji/', views.my_favourite_emodji_view),
    path('about_my_self/', views.about_my_self_view),
    
    path('blog_list/', views.blog_list_view),
    path('blog_list/<int:id>/', views.blog_detail_view),
    path('search/', views.blog_search_view),
]