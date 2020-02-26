from django.urls import path, include

from .views import (
        events_list,
        event_detail,
        register_to_event,
        thank_you,
        )

app_name = 'events'

urlpatterns = [
    path('', events_list, name='home'),
    path('list/thank_you', thank_you, name='thank_you'),
    path('list/register_to_event', register_to_event, name='register_to_event'),
    path('list/<int:event_id>', event_detail, name='details'),


]
