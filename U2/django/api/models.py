from django.db import models

class Motos(models.Model):
    PRESUPUESTO_CHOICES = [
        ('Bajo', 'Bajo'),
        ('Medio', 'Medio'),
        ('Alto', 'Alto'),
    ]
    
    POTENCIA_CHOICES = [
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),
    ]
    
    USO_CHOICES = [
        ('Esporádico', 'Esporádico'),
        ('Regular', 'Regular'),
        ('Frecuente', 'Frecuente'),
        ('Muy frecuente', 'Muy frecuente'),
    ]
    
    ZONA_CHOICES = [
        ('Rural', 'Rural'),
        ('Urbano', 'Urbano'),
        ('Semi-Urbano', 'Semi-Urbano'),
    ]
    
    SALIDA_CHOICES = [
        ('Deportiva', 'Deportiva'),
        ('Doble propósito', 'Doble propósito'),
        ('Trabajo', 'Trabajo'),
    ]
    
    presupuesto = models.CharField(max_length=10, choices=PRESUPUESTO_CHOICES)
    potencia = models.CharField(max_length=10, choices=POTENCIA_CHOICES)
    uso = models.CharField(max_length=15, choices=USO_CHOICES)
    zona = models.CharField(max_length=12, choices=ZONA_CHOICES)
    salida = models.CharField(max_length=15, choices=SALIDA_CHOICES)

    