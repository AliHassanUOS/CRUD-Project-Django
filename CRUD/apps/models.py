from django.db import models

# Create your models here.

class Student(models.Model):

    name = models.CharField(max_length=50)
    roll_num = models.IntegerField()
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f" Student -> {self.name} And Student Roll is --> {self.roll_num} "


