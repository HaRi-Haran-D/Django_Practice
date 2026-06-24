from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Task(models.Model):
    student_ref = models.ForeignKey(Student, related_name='all_task', null=True, on_delete=models.CASCADE)
    taskname = models.CharField(max_length=250)
    description = models.TextField()


class RankSheet(models.Model):
    tamil = models.IntegerField()
    english = models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()
    social = models.IntegerField()
    total = models.IntegerField()
    average = models.IntegerField()
    result = models.BooleanField()
