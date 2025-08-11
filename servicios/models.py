from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.


class Servicio(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    descripcion = CKEditor5Field(
        verbose_name='Descripción',
        config_name='default',
        help_text='Descripción del servicio'
    )
    imagen = models.ImageField(upload_to='servicios', verbose_name='Imagen')
    menu = models.BooleanField(default=False, verbose_name='Activo')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')    

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('servicios:servicio_detail', kwargs={'slug': self.slug})
