from django.db import models

# Create your models here.
class comprobante(models.Model):
    idcomprobante=models.CharField(max_length=20,primary_key=True)
    usuario=models.CharField(max_length=20)
    total= models.FloatField()
    idcliente = models.CharField(max_length=10)
    fecha=models.DateField()

