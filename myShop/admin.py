from django.contrib import admin
from .models import Product, SerialNumber, ProductComment


admin.site.register(Product)
admin.site.register(SerialNumber)
admin.site.register(ProductComment)