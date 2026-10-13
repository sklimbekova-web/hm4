from django.db import models
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name



class Tour(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название тура")
    date = models.DateField(verbose_name="Дата тура") 
    description = models.TextField(verbose_name="Описание")
    categories = models.ManyToManyField(Category, related_name="tours", verbose_name="Категории")

    def __str__(self):
        return f"{self.title} ({self.date})"




class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя человека")
    tour = models.OneToOneField(
        Tour, 
        on_delete=models.CASCADE, 
        verbose_name="Купленный тур"
    )
    ticket_number = models.CharField(max_length=50, unique=True, verbose_name="Номер билета")

    def __str__(self):
        return f"{self.name} (Билет: {self.ticket_number})"




class Comment(models.Model):
    text = models.TextField(verbose_name="Текст отзыва")
    tour = models.ForeignKey(
        Tour, 
        on_delete=models.CASCADE, 
        related_name="comments", 
        verbose_name="Тур"
    )
    person = models.ForeignKey(
        Person, 
        on_delete=models.CASCADE, 
        related_name="comments", 
        verbose_name="Автор отзыва"
    )

    def __str__(self):
        return f"Отзыв от {self.person.name} на {self.tour.title}"