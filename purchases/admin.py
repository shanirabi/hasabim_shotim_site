from django.contrib import admin

from .models import Purchase


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'purchase_date', 'vendor','product','quantity','price','payment_method','actual_payment_date','notes']
    readonly_fields = ('total_cost',)

admin.site.register(Purchase, PurchaseAdmin)
