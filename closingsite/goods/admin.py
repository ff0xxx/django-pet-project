from django.contrib import admin
from goods.models import Categories, Products

# Register your models here.

# admin.site.register(Categories)
# admin.site.register(Product)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'quantity', 'price', 'discount']
    list_editable = ['discount',]
    fields = [
        'name',
        'slug',
        'description',
        'image',
        ('price', 'discount'),
        'quantity',
        'category'
    ]