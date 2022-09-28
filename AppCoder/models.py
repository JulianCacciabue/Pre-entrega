from django.db import models

# Create your models here.


class Relojes(models.Model):

    nombre = models.CharField(max_length=60)
    modelo = models.IntegerField()
    
class billeteras(models.Model):
    #pass
    nombreBilletera = models.CharField(max_length=60)

class lentes(models.Model):
    #pass

    nombreLentes = models.CharField(max_length=60)

class Ejemplo(models.Model):

    nombreEjemplo = models.CharField(max_length=60)