from django.db import models

class Book(models.Model):
    title = models.CharField(verbose_name='Название книги:', max_length=100,)
    author = models.CharField(verbose_name='Автор книги:', max_length=40)
    description = models.TextField(verbose_name='Описание книги:', )
    publication_date = models.DateField(verbose_name='Дата публикации:')
    pages = models.IntegerField(verbose_name='Количество страниц:')
    price = models.DecimalField(verbose_name='Цена книги:', max_digits=8, decimal_places=2)
    rating = models.FloatField(verbose_name='Рейтинг книги:', default=0)
    genre = models.CharField(verbose_name='Жанр:', max_length=100)
    publisher_email = models.EmailField(verbose_name="Email издательства", blank=True)
    website_url = models.URLField(verbose_name="Сайт книги", blank=True)
    views = models.PositiveBigIntegerField(default=0, null = True)
    

    def __str__(self):
        return self.title
   

