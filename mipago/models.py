from django.db import models

class Pago(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    fecha_vencimiento = models.DateField()
