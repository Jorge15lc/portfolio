from django.db import models
from django.db import models
from django.utils.translation import gettext_lazy as _

class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Título"), help_text=_("Ingrese el título del servicio"))
    icon = models.CharField(max_length=50, verbose_name=_("Ícono"), help_text=_("Ingrese el ícono del servicio"))
    description = models.TextField(verbose_name=_("Descripción"), help_text=_("Ingrese la descripción del servicio"))
    modal_image = models.ImageField(upload_to='services/', verbose_name=_("Imagen Modal"), help_text=_("Seleccione la imagen para el modal"))
    modal_subtitle = models.CharField(max_length=100, default="SERVICIOS", verbose_name=_("Subtítulo Modal"), help_text=_("Ingrese el subtítulo para el modal"))
    modal_title = models.CharField(max_length=100, verbose_name=_("Título Modal"), help_text=_("Ingrese el título para el modal"))
    modal_content = models.TextField(verbose_name=_("Contenido Modal"), help_text=_("Ingrese el contenido para el modal"))
    process_title = models.CharField(max_length=100, verbose_name=_("Título del Proceso"), help_text=_("Ingrese el título para el proceso"))
    process_description = models.TextField(verbose_name=_("Descripción del Proceso"), help_text=_("Ingrese la descripción para el proceso"))
    process_steps = models.TextField(verbose_name=_("Pasos del Proceso"), help_text=_("Ingrese los pasos para el proceso"))
    additional_info = models.TextField(blank=True, null=True, verbose_name=_("Información Adicional"), help_text=_("Ingrese información adicional (opcional)"))

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("Servicio")
        verbose_name_plural = _("Servicios")
        ordering = ['id']