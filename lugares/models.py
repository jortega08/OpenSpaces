from django.db import models

class TipoLugar(models.Model):
    OPCIONES_TIPO = [
        ('parque', 'Parque'),
        ('auditorio', 'Auditorio'),
        ('salon', 'Salón'),
        ('campo', 'Campo'),
    ]

    nombre = models.CharField(
        max_length=50,
        unique=True,
        choices=OPCIONES_TIPO,
        verbose_name="Tipo de Lugar"
    )

    def __str__(self):
        return self.get_nombre_display()
    
class Lugar(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    capacidad = models.IntegerField()

    DISPONIBLE = 'disponible'
    OCUPADO = 'ocupado'
    ESTADO_CHOICES = [
        (DISPONIBLE, 'Disponible'),
        (OCUPADO, 'Ocupado'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default=DISPONIBLE)
    tipo_espacio = models.ForeignKey(TipoLugar, on_delete=models.SET_NULL, null=True, related_name='espacios')

    def __str__(self):
        return self.nombre

