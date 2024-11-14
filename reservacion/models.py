from django.db import models
from django.core.exceptions import ValidationError
from datetime import timedelta
from lugares.models import Lugar

class Reserva(models.Model):
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, related_name='reservas')
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE, related_name='reservas')
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def clean(self):
        # hora de fin es mayor a la de inicio
        if self.hora_fin <= self.hora_inicio:
            raise ValidationError("La hora de fin debe ser posterior a la hora de inicio.")
        
        # la reserva no exceda 2 horas
        duracion = timedelta(
            hours=self.hora_fin.hour, minutes=self.hora_fin.minute
        ) - timedelta(hours=self.hora_inicio.hour, minutes=self.hora_inicio.minute)
        if duracion > timedelta(hours=2):
            raise ValidationError("La duración de la reserva no puede exceder las 2 horas.")
        
        # verificar si ya existe una reserva en el mismo lugar y con el mismo horario
        reservas_existentes = Reserva.objects.filter(
            lugar=self.lugar,
            fecha=self.fecha
        ).filter(
            (models.Q(hora_inicio__lt=self.hora_fin) & models.Q(hora_fin__gt=self.hora_inicio))
        )
        
        if reservas_existentes.exists():
            raise ValidationError(f"El lugar {self.lugar.nombre} ya está reservado en esa fecha y hora.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Reserva de {self.usuario.username} en {self.lugar.nombre} el {self.fecha}'

