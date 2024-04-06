from django.db import models

class Venta(models.Model):
    barrio=models.CharField(max_length=120)
    mes=models.CharField(max_length=120)