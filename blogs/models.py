from django.db import models

# Create your models here.
class Blog(models.Model):
        image = models.ImageField(upload_to='images/', null=True)
        title = models.CharField(max_length=100)
        author = models.CharField(max_length=100, null=True)
        slug = models.SlugField()
        # description = models.TextField(null=True)
        body = models.TextField()
        time_to_read_min = models.IntegerField(null=True)
        date = models.DateTimeField(auto_now_add=True)

        def snippet(self):
            return self.body[:50] + '... '
