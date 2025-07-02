from django.db import models

# Create your models here.
from django.db import models

class Perro(models.Model):
    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('reservado', 'Reservado'),
        ('adoptado', 'Adoptado'),
    ]
    
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    tamaño = models.CharField(max_length=50)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    estado_salud = models.CharField(max_length=100)
    vacunado = models.BooleanField(default=False)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='disponible')
    temperamento = models.CharField(max_length=100)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.raza})"

class UsuarioAdoptante(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    dni = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()
    
    # Preferencias
    raza_preferida = models.CharField(max_length=100, blank=True, null=True)
    tamaño_preferido = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Adopcion(models.Model):
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(UsuarioAdoptante, on_delete=models.CASCADE)
    fecha_adopcion = models.DateTimeField(auto_now_add=True)
    completada = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Adopción de {self.perro} por {self.usuario}"