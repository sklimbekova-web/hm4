from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название жанра")
    slug = models.SlugField(unique=True, verbose_name="URL Slug")

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название фильма")
    description = models.TextField(verbose_name="Описание")
    poster = models.ImageField(upload_to="posters/", verbose_name="Постер")
    release_year = models.PositiveIntegerField(verbose_name="Год выпуска")
    duration_minutes = models.PositiveIntegerField(verbose_name="Длительность (мин)")
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        verbose_name="Рейтинг (0-10)"
    )
    genres = models.ManyToManyField(Genre, related_name="movies", verbose_name="Жанры")

    def __str__(self):
        return self.title

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="comments", verbose_name="Фильм")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", verbose_name="Автор")
    text = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True)

class VipSeat(models.Model):
    seat_number = models.PositiveIntegerField(unique=True, verbose_name="Номер VIP-места")
    reserved_by = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="vip_seat", verbose_name="Кто занял"
    )

    def __str__(self):
        return f"VIP Место №{self.seat_number}"