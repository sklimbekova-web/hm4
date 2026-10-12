from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models


def blog_list_view(request):
    if request.method == 'GET':
        blog = models.Blog.objects.all()
    return render(request, 'blog_list.html', {'blog': blog})


def blog_detail_view(request, id):
    if request.method == 'GET':
        blog_id = get_object_or_404(models.Blog, id=id)
    return render(request, 'blog_detail.html', {'blog_id': blog_id})


def hello_world_view(request):
    if request.method == "GET":
        return HttpResponse('Ура это первый мой проект на DJANGO')

def my_favourite_emodji_view(request):
    if request.method == "GET":
        return HttpResponse('😁🤣🤖🫠🌚')

def about_my_self_view(request):
    if request.method == 'GET':
        return HttpResponse('Меня зовут Галя, я BACKEND DEVELOPER')

def book_list_view(request):
    if request.method == 'GET':
        books = Book.object.all()
        return render (request, 'book_list.html', {'books': books})

def book_detail_view(request, book_id):
    book = get_object_or_404(Book, book_id)
    return render(request, 'book_detail_html', {'book': book}) 
