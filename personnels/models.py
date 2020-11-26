from django.db import models

# Create your models here.
class Personnels(models.Model):
    identite = models.CharField(max_length=200)
    poste = models.CharField(max_length=200)
    adresse_mail = models.CharField(max_length=200)
    photo_url = models.CharField(max_length=5000)