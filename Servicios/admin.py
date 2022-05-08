from django.contrib import admin
from .models import Servicio

# Register your models here.
class ServiciosAdmin(admin.ModelAdmin):   
    readonly_fields = ("created", "updated")   # Para poder ver esos campos en el panel de adm solo para lectura. Sino no aparecen

admin.site.register(Servicio, ServiciosAdmin)
