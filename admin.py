from django.contrib import admin
from .models import Perro, UsuarioAdoptante, Adopcion

@admin.register(Perro)
class PerroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'raza', 'edad', 'estado')
    list_filter = ('raza', 'estado')
    search_fields = ('nombre', 'raza')

@admin.register(UsuarioAdoptante)
class UsuarioAdoptanteAdmin(admin.ModelAdmin):
    list_display = ('user', 'dni', 'telefono')
    search_fields = ('user__username', 'dni')

@admin.register(Adopcion)
class AdopcionAdmin(admin.ModelAdmin):
    list_display = ('perro', 'usuario', 'fecha_adopcion', 'completada')
    list_filter = ('completada',)