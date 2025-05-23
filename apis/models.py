from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
