from django.contrib import admin

from .models import Vendor

# Register your models here.
# class VendorAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Vendor._meta.get_fields()]

admin.site.register(Vendor)
