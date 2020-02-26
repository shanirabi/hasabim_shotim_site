from django.urls import path

from .views import (
        ProductListView,
        ProductDetailSlugView,
        )

urlpatterns = [
        path('<slug>/', ProductDetailSlugView.as_view(),name='detail'),
        path('', ProductListView.as_view(), name='products'),
]
