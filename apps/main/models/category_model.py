from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _

class Category(TimeStampedModel):
    name = models.CharField(
        max_length=100,
        verbose_name=_("Nombre"),
        help_text=_("El nombre de la categoría.")
    )

    active = models.BooleanField(
        default=True, 
        verbose_name=_("Activo"), 
        help_text=_("El estado activo de la categoría.")
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Categoría")
        verbose_name_plural = _("Categorías")
        ordering = ['name']