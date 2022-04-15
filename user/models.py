from django.db import models


# Create your models here.
#  model created for user form
class User(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateField(null=True)
    email = models.EmailField(max_length=120)
    income = models.PositiveIntegerField()
    ipaddress = models.GenericIPAddressField()
