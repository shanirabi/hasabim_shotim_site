from django.db import models

# Create your models here.
class City(models.Model):
    city_symbol                 = models.IntegerField()
    city_name_hebrew            = models.CharField(max_length=240, unique=True)
    city_name_english           = models.CharField(max_length=240)
    city_name_transcription     = models.CharField(max_length=240)
    district                    = models.CharField(max_length=240)
    subdistrict_name            = models.CharField(max_length=240)
    subdistrict_symbol	        = models.IntegerField()
    data_year                   = models.IntegerField(default='2018')

    def __str__(self):
        return self.city_name_hebrew
