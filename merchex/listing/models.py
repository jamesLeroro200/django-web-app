from unicodedata import name
from django.db import models

class Band(models.Model):
    name = models.fields.CharField(max_length=100)


class Listings(models.Model):
    titre = models.fields.CharField(max_length=100)
        
