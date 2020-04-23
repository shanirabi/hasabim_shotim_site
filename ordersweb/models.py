from django.db import models
from carts.models import Cart

from django.db.models.signals import pre_save, post_save
from ecommerce.utils import unique_order_id_generator

# Create your models here.

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('created', 'Created'),
    ('refunded', 'Refunded'),
)

DELIVERY_METHOD_CHOICES = (
    ('pickup', 'איסוף עצמי'),
    ('shipping', 'משלוח בתשלום'),
)
class OrderWeb(models.Model):
    order_submitted_date = models.DateTimeField(auto_now_add=True, blank=True)
    order_id            = models.CharField(max_length=120, blank=True) # AB31DE3
    cart            = models.ForeignKey(Cart,  on_delete=models.CASCADE, null=True, blank=True)
    status          = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES, null=True, blank=True)
    first_name      = models.CharField(max_length=120, null=True, blank=True)
    last_name       = models.CharField(max_length=120, null=True, blank=True)
    phone_number    = models.CharField(max_length=15, null=True, blank=True)
    email           = models.EmailField( null=True, blank=True)
    delivery_method = models.CharField(max_length=120, choices=DELIVERY_METHOD_CHOICES, null=True, blank=True)
    address_line_1  = models.CharField(max_length=120, null=True, blank=True)
    # address_line_2  = models.CharField(max_length=120, null=True, blank=True)
    city            = models.CharField(max_length=120, null=True, blank=True)
    country         = models.CharField(max_length=120, default='ישראל', null=True, blank=True)
    postal_code     = models.CharField(max_length=120, null=True, blank=True)
    age_above_18    = models.BooleanField(default=True)
    shipping_cost   = models.DecimalField(default=0, max_digits=100, decimal_places=2, null=True, blank=True)
    order_cost      = models.DecimalField(default=0, max_digits=100, decimal_places=2, null=True, blank=True)
    shipping_date   = models.DateTimeField(null=True, blank=True)
    pickup_date   = models.DateTimeField(null=True, blank=True)

    def _get_total(self):
        return self.order_cost + self.shipping_cost

    total_cost = property(_get_total)

def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)


pre_save.connect(pre_save_create_order_id, sender=OrderWeb)
