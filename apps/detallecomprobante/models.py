from django.db import models

# Create your models here.
class detallecomprobante(models.Model):
    idcomprobante = models.CharField(max_length=20,primary_key=True)
    idproducto=models.CharField(max_length=25)
    cantidad= models.IntegerField()
    importe=models.FloatField()
