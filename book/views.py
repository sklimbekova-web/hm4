from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from django.core.paginator import Paginator
from django.db.models import F

def blog_search_view(request):
    query = request.GET.get('q','')
    if query:
        blog = models.Blog.object.all()
    else:
        return HttpResponse('Блог не найден')
    

class SearchView()




# def blog_list_view(request):
    if request.method == 'GET':
        blog = models.Blog.objects.all()
        Paginator_blog = Paginator(blog, 2)
        page = request.GET.get('page')
        page_obj = paginator_blog.get_page(page)
    return render(request, 'blog_list.html', {'blog': page_obj})


def blog_detail_view(request, id):
    if request.method == 'GET':
        blog_id = get_object_or_404(models.Blog, id=id)
        views_blog = request.sessions.get('viewed_blog', [])
        if id not in views_blog:
            blog_id.view = F("views") + 1
            blog_id.save()
            blog_id.refresh_from_db()
        views_blog.append(id)
        request.sessions['viewed_blog'] = views_blog



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
