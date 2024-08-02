from django.db import models


class Lote(models.Model):
    medicamento = models.CharField(max_length=255)
    fecha_vencimiento = models.DateField()
    codigo = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField()
    def __str__(self) -> str:
        return self.codigo
    pass


class Consumo(models.Model):
    pass


class Stock(models.Model):
    pass


class Movimiento(models.Model):
    pass
