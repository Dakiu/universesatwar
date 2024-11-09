from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Usuario(models.Model):
    acciones = models.IntegerField(default=100)
    poder = models.IntegerField(default=100)
    oro = models.IntegerField(default=100)
    recursos = models.IntegerField(default=0)
    poder = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE) 

class Tripulacion(models.Model):
    nombre = models.CharField(max_length=30)
    imagen = models.CharField(max_length=255, default="")
    ataque= models.IntegerField(default=0)
    defensa = models.IntegerField(default=0)
    radar = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    poder = models.IntegerField(default=0)
    asignado = models.BooleanField(default=False)

class Nave(models.Model):
    nombre = models.CharField(max_length=30) 
    ataque = models.IntegerField(default=0)
    defensa = models.IntegerField(default=0)
    escudos = models.IntegerField(default=0)
    radar = models.IntegerField(default=0)
    comunicaciones = models.IntegerField(default=0)
    resistencia = models.IntegerField(default=20)
    capacidadTripulantes = models.IntegerField(default=6)

class Nave_Usuario(models.Model):
    Nave = models.ForeignKey(Nave, on_delete=models.CASCADE)
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    resistencia = models.IntegerField(default=0)
    ataque = models.IntegerField(default=0)
    defensa = models.IntegerField(default=0)
    escudos = models.IntegerField(default=0)
    radar = models.IntegerField(default=0)
    comunicaciones = models.IntegerField(default=0)

class Tripulacion_Usuario(models.Model):
    Tripulacion = models.ForeignKey(Tripulacion, on_delete=models.CASCADE)
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
class RegistroBatalla(models.Model):
    atacante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='atacante')
    defensor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='defensor')
    relatoBatalla = models.TextField()
    fecha = models.DateField(auto_now_add=True)


