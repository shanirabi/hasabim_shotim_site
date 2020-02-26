from django.contrib import admin
from .models import Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Blog._meta.get_fields()]

admin.site.register(Blog, BlogAdmin)
