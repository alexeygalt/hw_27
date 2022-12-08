import json

from django.db import models


class Ads(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    is_published = models.BooleanField(default=False)


class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)



