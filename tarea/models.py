from django.db import models

class Tarea(models.Model):
    ESTADO_CHOICES=(
        ('pendiente', 'Pendiente'),
        ('completada', 'Completada')
    )
    fecha=models.DateTimeField(auto_now_add=True)
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField(null=True, blank=True, default="sin Descripcion")
    estado=models.CharField(max_length=50, choices=ESTADO_CHOICES, default='pendiente')
    
    def __str__(self):
        return self.nombre