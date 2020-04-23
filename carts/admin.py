from django.contrib import admin

from .models import Cart, CartItems

class CartAdmin(admin.ModelAdmin):
    list_display = ['id','total']


class CartItemsAdmin(admin.ModelAdmin):
    list_display = ['cart','product',  'quantity', 'quantity_total']
    class Meta:
        model = CartItems

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItems, CartItemsAdmin)
