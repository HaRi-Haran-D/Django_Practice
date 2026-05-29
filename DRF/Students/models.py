from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Task(models.Model):
    taskname = models.CharField(max_length=250)
    description = models.TextField()