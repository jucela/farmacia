from django.db import models
from apps.proveedor.models import proveedor
from apps.presentacion.models import presentacion

# Create your models here.
class medicamento(models.Model):
    tipo_choices = (
        ('Comercial', 'Comercial'),
        ('Generico', 'Generico'),

    )
    # id_medicamento = models.AutoField(primary_key=True)---no regresa el id
    id_medicamento = models.IntegerField(primary_key=True)
    tipo=models.CharField(max_length=50,choices=tipo_choices)
    nombre_comercial=models.CharField(max_length=50)
    componente = models.CharField(max_length=100)
    concentracion = models.CharField(max_length=50)
    fecha_produccion = models.CharField(max_length=50)
    fecha_expiracion = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    stock = models.IntegerField()
    costo_unidad = models.FloatField()
    venta_unidad = models.FloatField()
    proveedor = models.ForeignKey(proveedor,null=True,blank=True,on_delete=models.CASCADE)
    presentacion=models.ForeignKey(presentacion,null=True,blank=True,on_delete=models.CASCADE)
    lote = models.CharField(max_length=50)
    estado=models.BooleanField()
