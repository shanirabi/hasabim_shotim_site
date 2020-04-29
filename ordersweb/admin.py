from django.contrib import admin

from .models import OrderWeb

# Register your models here.

class OrderWebAdmin(admin.ModelAdmin):
    readonly_fields = ('total_cost','cart')
    list_display = ['cart', 'order_submitted_date', 'status', 'order_cost', 'last_name', 'first_name','phone_number','email', 'delivery_method', 'total_cost']



admin.site.register(OrderWeb,OrderWebAdmin )
