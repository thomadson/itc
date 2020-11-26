from django.db import models

# Create your models here.
class Services(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.CharField(max_length=5000)