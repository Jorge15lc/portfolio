from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field

class Work(TimeStampedModel):
    title = models.CharField(
        max_length=200,
        verbose_name=_("Título"),
        help_text=_("El título del trabajo.")
    )
    description = CKEditor5Field(
        verbose_name=_("Descripción"),
        help_text=_("La descripción del trabajo.")
    )
    def upload_to(instance, filename):
        return f"portfolio/{instance.title}/{filename}"
    
    image = models.ImageField(
        upload_to=upload_to,
        verbose_name=_("Imagen"),
        help_text=_("La imagen del trabajo.")
    )
    client = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name=_("Cliente"),
        help_text=_("El cliente del trabajo.")
    )
    categories = models.ManyToManyField(
        'Category',
        related_name='works',
        verbose_name=_("Categorías"),
        help_text=_("Las categorías del trabajo.")
    )
    start_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=_("Fecha de inicio"),
        help_text=_("La fecha de inicio del trabajo.")
    )
    website = models.URLField(
        blank=True,
        null=True,
        verbose_name=_("Sitio web"),
        help_text=_("El sitio web del trabajo.")
    )
    designer = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name=_("Diseñador"),
        help_text=_("El diseñador del trabajo.")
    )
    project_description = CKEditor5Field(
        blank=True,
        null=True,
        verbose_name=_("Descripción del proyecto"),
        help_text=_("La descripción del proyecto del trabajo.")
    )
    story = CKEditor5Field(
        blank=True,
        null=True,
        verbose_name=_("Historia"),
        help_text=_("La historia del trabajo.")
    )
    approach = CKEditor5Field(
        blank=True,
        null=True,
        verbose_name=_("Enfoque"),
        help_text=_("El enfoque del trabajo.")
    )
    gallery_images = models.ManyToManyField(
        'GalleryImage',
        blank=True,
        verbose_name=_("Imágenes de la galería"),
        help_text=_("Las imágenes de la galería del trabajo.")
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("Trabajo")
        verbose_name_plural = _("Trabajos")
        ordering = ['-created']


class GalleryImage(TimeStampedModel):

    def upload_to(instance, filename):
        return f"portfolio/gallery/{filename}"
    
    image = models.ImageField(
        upload_to=upload_to,
        verbose_name=_("Imagen"),
        help_text=_("La imagen de la galería.")
    )

    def __str__(self):
        return f"Imagen de la galería {self.id}"
    
    class Meta:
        verbose_name = _("Imagen de la galería")
        verbose_name_plural = _("Imágenes de la galería")
        ordering = ['-created']
