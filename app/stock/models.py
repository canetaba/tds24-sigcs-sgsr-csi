from django.db import models
from maestro.models import Medicamento, Institucion
from datetime import date


class Lote(models.Model):
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    fecha_vencimiento = models.DateField()
    codigo = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.codigo


class Consumo(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    fecha = models.DateField(default=date.today)
    cantidad = models.PositiveIntegerField()


class Stock(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
    fecha_actualizacion = models.DateField(default=date.today)
    has_quiebre = models.BooleanField(default=False)

    class Meta:
        unique_together = [("institucion", "medicamento")]


class Movimiento(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    fecha = models.DateField(default=date.today)
    lote = models.OneToOneField(Lote, unique=True, on_delete=models.CASCADE)
