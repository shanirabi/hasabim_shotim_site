"""ecommerce URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from accounts.views import login_page, register_page, guest_register_view
from carts.views import cart_home, cart_update, checkout_done_view
from events.views import register_to_event
from blogs.views import blog_list, blog_detail
# from partners.views import partners_list
from .views import homepage, contact, about, logout_request, terms
from addresses.views import checkout_address_create_view, checkout_address_reuse_view
from vendors.views import vendors_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name = "homepage"),
    path('login/', login_page, name = "login_page"),
    path("logout/", logout_request, name="logout"),
    path('register/guest', guest_register_view, name = "guest_register"),
    path('register/', register_page, name = "register_page"),
    path('contact/', contact, name = "contact"),
    path('about/', about, name="about"),
    path('cart/customer_info/terms', terms, name="terms"),
    path('products/', include("products.urls")),
    path('cart/', include('carts.urls')),
    path('events/', include('events.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('blog/', blog_list, name="blog_list"),
    path('blog/<int:blog_id>', blog_detail, name='blog_detail'),
    path('vendors/', vendors_list, name="vendors_list"),
    path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
    path('checkout/address/reuse/', checkout_address_reuse_view, name='checkout_address_reuse'),
    path('checkout/success/', checkout_done_view, name='success'),



    # path('cart/', cart_home, name='cart'),
    # path('cart/update', cart_update, name='update'),


    # path('featured/', ProductFeaturedListView.as_view()),
    # path('featured/<pk>/', ProductFeaturedDetailView.as_view()),
    # path('products/<slug>/', ProductDetailSlugView.as_view()),
    # path('products/', ProductListView.as_view()),
    # path('products-fbv/', product_list_view, name='product_list_view'),
    # # path('products/<pk>/', ProductDetailView.as_view()),
    # path('products-fbv/<pk>/', product_detail_view),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
