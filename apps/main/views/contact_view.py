from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib import messages
from ..forms import ContactForm


class ContactView(CreateView):
    template_name = 'contact/contact.html'
    form_class = ContactForm  # Formulario que se utilizará
    success_url = reverse_lazy('main:home')  # Redirige a esta URL después de enviar el formulario

    def form_valid(self, form):
        # Guardar el formulario en la base de datos
        form.save()
        # Mostrar un mensaje de éxito
        messages.success(self.request, _('Tu mensaje ha sido enviado con éxito.\n Nos pondremos en contacto contigo lo antes posible.'))
        # Llamar a la implementación base para completar la validación
        return super().form_valid(form)
