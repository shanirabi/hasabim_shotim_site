from django.contrib import admin

from .models import Cart, CartItems

class CartItemsAdmin(admin.ModelAdmin):
    list_display = ['__str__','product', 'cart', 'quantity', 'quantity_total']
    class Meta:
        model = CartItems

admin.site.register(Cart)
admin.site.register(CartItems, CartItemsAdmin)
