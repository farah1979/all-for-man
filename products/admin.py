from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """ class to display all informations
    about the product in admin pannel"""
    list_display = (
        'category',
        'sku',
        'name',
        'price',
        'volym',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """ to show all we want about the categories in admin pannel"""
    list_display = (
        'name',
        'friendly_name',
        'description',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
