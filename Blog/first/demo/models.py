from django.db import models

# Create your models here.
class BlogPost(models.Model):
    post_title = models.CharField(max_length=100)
    post_image = models.ImageField(upload_to='images')