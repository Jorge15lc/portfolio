from django.db import models
from django_extensions.db.models import TimeStampedModel

class Contact(TimeStampedModel):
    first_name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, verbose_name="Apellido")
    email = models.EmailField(verbose_name="Correo Electrónico")
    phone = models.CharField(max_length=15, verbose_name="Número de Teléfono")
    service = models.CharField(max_length=50, verbose_name="Servicio")
    message = models.TextField(verbose_name="Mensaje")

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'