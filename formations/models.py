from django.db import models

# Create your models here.
class Formations(models.Model):
    lib_fomration = models.CharField(max_length=200)
    module_formation = models.TextField()

