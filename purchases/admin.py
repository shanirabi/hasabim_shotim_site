from django.contrib import admin

from .models import Purchase


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'purchase_date', 'vendor','product','quantity','price', 'total_amount','payment_method','actual_payment_date','notes']
    class Meta:
        model = Purchase

admin.site.register(Purchase, PurchaseAdmin)
