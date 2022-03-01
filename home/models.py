from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=10)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class Add(models.Model):
    num = models.IntegerField(blank=True, null=True)
    prod_name = models.CharField(max_length=120)
    price = models.IntegerField(blank=True, null=True)
