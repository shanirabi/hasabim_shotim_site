from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','vendor', 'year', 'price', 'active', 'slug']
    list_filter =  ['vendor', 'year', 'price', 'active', 'type']
    search_fields = ['title']

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
admin.site.unregister(Group)
