from django.shortcuts import render,redirect
from .models import Cart, Product, CartItems
from addresses.models import Address
from orders.models import Order
from accounts.forms import LoginForm, GuestForm
from billing.models import BillingProfile
from accounts.models import GuestEmail
from addresses.forms import AddressForm
from ordersweb.models import OrderWeb
from ordersweb.forms import OrderWebForm

from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse


# def cart_create(user=None):
#     cart_obj = Cart.objects.create(user=None)
#     print('New Cart created')
#     return cart_obj

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    #FOLLOWING CHANGE
    #TO DISPLAY THE CART VALUES QUANTITY WISE
    #WITH CALCULATED TOTAL
    item_obj = CartItems.objects.filter(cart=cart_obj)
    total = 0
    for item in item_obj:
        print(item.product, item.quantity,item.get_total())
        total += item.get_total()

    cart_obj.total=total
    cart_obj.save()
    return render(request, "carts/home.html", {"cart": cart_obj, "items": item_obj, "total": total})

def cart_update(request):
    product_id = request.POST.get('product_id')
    #FOLLOWING CHANGE
    #TOOK THE QUANTITY VALUE FROM FORM POST VALUES
    number = request.POST.get('number')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Show message to user, product is gone?")
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if 'remove' in request.POST:
            item = CartItems.objects.get(product_id=product_id,cart=cart_obj)
            item.delete()
            cart_obj.products.remove(product_obj)
        else:

            #IF THE ITEM ALREADY EXIST UPDATE ITS QUANTITY
            #ELSE CREATE THE NEW OBJECT WITH ASSIGNED QUANTITY
            try:
                item = CartItems.objects.get(product=product_obj,cart=cart_obj)
                item.quantity = number
                item.save()
            except:
                item = CartItems.objects.create(product=product_obj,cart=cart_obj, quantity=number)
                cart_obj.products.add(product_obj) # cart_obj.products.add(product_id)


        request.session['cart_items'] = cart_obj.products.count()
        # return redirect(product_obj.get_absolute_url())
    return redirect("carts:home")



def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None

    if cart_created or cart_obj.products.count() == 0:
        return redirect("carts:home")

    login_form = LoginForm()
    guest_form = GuestForm()
    address_form = AddressForm()
    billing_address_id = request.session.get("billing_address_id", None)
    shipping_address_id = request.session.get("shipping_address_id", None)

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    address_qs = None
    if billing_profile is not None:
        if request.user.is_authenticated:
            address_qs = Address.objects.filter(billing_profile=billing_profile)
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
        if shipping_address_id:
            order_obj.shipping_address = Address.objects.get(id=shipping_address_id)
            del request.session["shipping_address_id"]
        if billing_address_id:
            order_obj.billing_address = Address.objects.get(id=billing_address_id)
            del request.session["billing_address_id"]
        if billing_address_id or shipping_address_id:
            order_obj.save()


    if request.method == "POST":
        "check that order is done"
        is_done = order_obj.check_done()
        if is_done:
            # order_obj.mark_paid()
            request.session['cart_items'] = 0
            del request.session['cart_id']
            return redirect("carts:payment", order_id=order_obj.order_id)
    context = {
        "object": order_obj,
        "billing_profile": billing_profile,
        "login_form": login_form,
        "guest_form": guest_form,
        "address_form": address_form,
        "address_qs": address_qs,
    }

    return render(request, "carts/checkout.html", context)

######
def customer_info(request):
    form = OrderWebForm()
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    item_obj = CartItems.objects.filter(cart=cart_obj)

    # for item in item_obj:
    #     print(item.product, item.quantity,item.get_total())

    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect("carts:home")
    else:
        order_obj, new_order_obj = Order.objects.get_or_create(cart=cart_obj)

    if request.method == "POST":
                # print(request.POST.get('first_name'))
                # print(request.POST.get('last_name'))
                id = cart_obj.id
                first_name = request.POST["first_name"]
                last_name = request.POST["last_name"]
                email = request.POST["email"]
                phone_number = request.POST["phone_number"]
                address_line_1 = request.POST["address_line_1"]
                # address_line_2 = request.POST["address_line_2"]
                city = request.POST["city"]
                # country = request.POST["country"]
                postal_code = request.POST["postal_code"]
                cart =  Cart.objects.get(id=id)
                order_cost      = cart_obj.total
                delivery_method = request.POST["delivery_method"]
                #save to db
                order_web = OrderWeb(first_name=first_name, last_name=last_name, email=email, phone_number = phone_number,
                                    address_line_1=address_line_1,city=city,postal_code=postal_code, cart=cart, order_cost=order_cost,
                                    delivery_method= delivery_method)
                order_web.save()


                #empty the cart
                request.session['cart_items'] = 0
                del request.session['cart_id']
    return render(request, "carts/customer_info.html", {"object": order_obj, 'form': form })

######

def payment(request, order_id):
    order = get_object_or_404(Order, order_id=str(order_id))
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': str(order.total),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('success')),
        "currency_code": "ILS",
        # 'cancel_return': 'http://{}{}'.format(host, reverse('payment_cancelled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    if form.is_valid():
        form.save()
        order.mark_paid()
    return render(request, 'carts/payment.html', {'order': order, 'form': form})



@csrf_exempt
def payment_canceled(request):
    return render(request, 'carts/cancelled.html')


def checkout_done_view(request):
    return render(request, "carts/checkout-done.html", {})
