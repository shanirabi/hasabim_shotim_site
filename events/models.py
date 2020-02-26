from django.db import models

# Create your models here.
class Event(models.Model):
        image = models.ImageField(upload_to='images/', null=True, blank = True)
        title = models.CharField(max_length=100)
        location = models.CharField(max_length=200)
        datetime_event = models.DateTimeField()
        description = models.TextField(null=True, blank=True)
        price = models.FloatField(max_length=6)
        date_added = models.DateTimeField(auto_now_add=True)

class EventRegistration(models.Model):
        REG_STATUS = [('submitted','submitted'),('confirmed','confirmed'), ( 'cancelled', 'cancelled'),]
        event_id = models.IntegerField()
        title = models.CharField(max_length=100)
        datetime_event = models.CharField(max_length=100)
        location = models.TextField(max_length=200)
        price = models.FloatField(max_length=15)
        fname = models.CharField(max_length=100)
        lname = models.CharField(max_length=100)
        eaddress = models.CharField(max_length=100)
        tel = models.CharField(max_length=15)
        num_of_people = models.CharField(max_length=15)
        # activity_registration_amount_shekel = models.FloatField(max_length=30)
        date_submitted = models.DateTimeField(auto_now_add=True)
        is_paid = models.BooleanField()
        registration_status = models.CharField(choices = REG_STATUS, max_length=20, default='submitted')
