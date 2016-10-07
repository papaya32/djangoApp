from __future__ import unicode_literals
from django.db import models

class Item(models.Model):
  name = models.CharField(max_length=20)
  icon = models.CharField(max_length=25)
  price = models.DecimalField(max_digits=4, decimal_places=2)

class User(models.Model):
  name = models.CharField(max_length=20)
  icon = models.CharField(max_length=25)
  tab = models.DecimalField(max_digits=6, decimal_places=2, default=0)
