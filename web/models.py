from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tripulacion(models.Model):
    nombre = models.CharField(max_length=30)
    imagen = models.CharField(max_length=70, default="")
    ataque= models.IntegerField(default=0)
    defensa = models.IntegerField(default=0)

