from django.db import models
#from .models import BookNumber

# Create your models here.
class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True, unique=True)
    isbn_13 = models.CharField(max_length=13, blank=True, unique=True)


class Book(models.Model):
    title = models.CharField(max_length=50, blank=False, unique=True)
    description = models.TextField(blank=True, max_length=250)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    published = models.DateField(blank=True, null=True, default=None)
    cover = models.ImageField(upload_to='covers/', blank=True)
    is_published = models.BooleanField(default=False)
    number = models.OneToOneField(BookNumber, null=True, blank=True, on_delete=models.CASCADE)
    #author = models.CharField(max_length=50)

    def __str__(self):
        return self.title


