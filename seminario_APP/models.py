from django.db import models

# Modelo para Institución
class Institucion(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

# Modelo para Inscritos
class Inscrito(models.Model):
    ESTADO_CHOICES = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO ASISTEN', 'No Asisten'),
    ]

    nombre_institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    numero_personas = models.PositiveIntegerField()
    telefono = models.CharField(max_length=15)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    hora_inscripcion = models.TimeField(auto_now_add=True)
    correo = models.EmailField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='RESERVADO')
    observacion = models.TextField(blank=True, null=True)
    persona_que_inscribe = models.CharField(max_length=100)  

    def __str__(self):
        return f"{self.nombre_institucion} - {self.estado}"
