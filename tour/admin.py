from django.contrib import admin
from .models import Category, Tour, Person, Comment

admin.site.register(Category)
admin.site.register(Tour)
admin.site.register(Person)
admin.site.register(Comment)
