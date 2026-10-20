from django.contrib import admin
from .models import Genre, Movie, Comment, VipSeat

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'rating')
    list_filter = ('genres', 'release_year')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('movie', 'author', 'created_at')

@admin.register(VipSeat)
class VipSeatAdmin(admin.ModelAdmin):
    list_display = ('seat_number', 'reserved_by')