from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50, blank=False, unique=True)
    description = models.TextField(blank=True, max_length=250)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    published = models.DateField(blank=True, null=True, default=None)
    cover = models.ImageField(upload_to='covers/', blank=True)
    is_published = models.BooleanField(default=False)
    #author = models.CharField(max_length=50)

    def __str__(self):
        return self.title
