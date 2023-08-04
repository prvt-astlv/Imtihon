from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created_at']
    ordering = ('created_at',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ('name',)
