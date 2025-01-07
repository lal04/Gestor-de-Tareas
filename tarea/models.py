from django.db import models

class Tarea(models.Model):
    fecha=models.DateTimeField(auto_now_add=True)
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField(null=True, blank=True, default="sin Descripcion")
    estado=models.BooleanField(default=False,)
    
    def __str__(self):
        return self.nombre