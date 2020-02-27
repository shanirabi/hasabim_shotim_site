from django.urls import path, include

from .views import (
        cart_home,
        cart_update,
        checkout_home,
        checkout_done_view,
        payment,
        payment_canceled
        )

app_name = 'carts'

urlpatterns = [
    path('', cart_home, name='home'),
    path('update/', cart_update, name='update'),
    path('checkout/', checkout_home, name='checkout'),
    path('process-payment/<str:order_id>/', payment, name='payment'),
    path('payment-cancelled/', payment_canceled, name='payment_cancelled'),
    path('checkout/success/', checkout_done_view, name='success'),
]



