from django.contrib import admin
from .models import Event, EventRegistration

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Event._meta.get_fields()]

class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EventRegistration._meta.get_fields()]

admin.site.register(Event, EventAdmin)
admin.site.register(EventRegistration, EventRegistrationAdmin)
