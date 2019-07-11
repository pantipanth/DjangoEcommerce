from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list.display = ('name', 'price', 'stock')


admin.site.register(Product, ProductAdmin)
