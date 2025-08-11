from django.contrib import admin
from .models import Servicio

# Register your models here.

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'imagen')
    prepopulated_fields = {'slug': ('titulo',)}
