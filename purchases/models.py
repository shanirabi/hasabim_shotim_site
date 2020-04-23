import random
import os
from django.db import models
from vendors.models import Vendor
from products.models import Product


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    # print(instance)
    #print(filename)
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )

PAYMENTS_TYPES = (
    ('credit_card', 'Credit Card'),
    ('check', 'Check'),
    ('bank_transfer', 'Bank Transfer'),
)

# Create your models here.
class Purchase(models.Model):
    purchase_date       = models.DateField()
    vendor              = models.ForeignKey(Vendor, max_length=200, on_delete=models.CASCADE)
    product             = models.ForeignKey(Product,max_length=200,on_delete=models.CASCADE)
    quantity            = models.IntegerField()
    price               = models.DecimalField(decimal_places=2, max_digits=20)
    # total_amount        = models.DecimalField(decimal_places=2, max_digits=20, blank=True, unique=True)
    payment_method      = models.CharField(max_length=200, choices=PAYMENTS_TYPES)
    actual_payment_date = models.DateField(blank=True)
    receipt_copy        = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    notes               = models.TextField(blank=True)

    def get_total(self):
        return self.purchase.price * self.quantity

    total_cost = property(get_total)
