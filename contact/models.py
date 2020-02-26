from django.db import models

# Create your models here.
class Contact(models.Model):
        fname = models.CharField(max_length=100)
        lname = models.CharField(max_length=100)
        eaddress = models.EmailField(max_length=150)
        tel = models.CharField(max_length=15)
        message = models.TextField()
        datetime = models.DateTimeField(auto_now_add=True)
