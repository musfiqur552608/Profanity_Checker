from django.db import models

# Create your models here.
class Profanity(models.Model):
    ctext = models.CharField(max_length=1000000)
    final = models.CharField(max_length=1000000)
    value = models.CharField(max_length=100, null=True)