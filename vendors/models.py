from django.db import models

# Create your models here.
class Vendor(models.Model):
    business_name            = models.CharField(max_length=120, null=True, blank=True, unique=True)
    business_address         = models.CharField(max_length=300, null=True, blank=True)
    business_phone           = models.CharField(max_length=120, null=True, blank=True)
    contact_name             = models.CharField(max_length=120, null=True, blank=True)
    contact_phone            = models.CharField(max_length=120, null=True, blank=True)
    logo                     = models.ImageField(upload_to='images/', null=True, blank=True)
    about                    = models.TextField(max_length=1000, null=True, blank=True)
    web_site                 = models.URLField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.business_name
