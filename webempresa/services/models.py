from django.db import models

# Create your models here.
class Service(models.Model):
    Title = models.CharField( max_length=200, verbose_name="Título")
    Subtitle = models.CharField( max_length=200, verbose_name="Subtítulo")
    Content = models.TextField(verbose_name="Contenido")
    Image= models.ImageField(verbose_name="Imagen", upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")
     # Para que se traduca y ponga bien el plural
    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ["-created"]
    def __str__(self):
        return self.Title
