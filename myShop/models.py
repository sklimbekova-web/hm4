from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock_quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    is_available = models.BooleanField(default=True, verbose_name="В наличии")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    sku = models.CharField(max_length=50, unique=True, verbose_name="Артикул")
    weight_kg = models.FloatField(verbose_name="Вес (кг)")

    def __str__(self):
        return self.title

class SerialNumber(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='serial_number')
    number = models.CharField(max_length=100, unique=True, verbose_name="Серийный номер")

    def __str__(self):
        return f"С/Н: {self.number} для {self.product.title}"

class ProductComment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100, verbose_name="Автор")
    text = models.TextField(verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв от {self.author}"