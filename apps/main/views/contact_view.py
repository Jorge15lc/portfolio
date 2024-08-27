from django.shortcuts import redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib import messages
from ..forms import ContactForm
from ..models import Contact


class ContactView(CreateView):
    template_name = 'contact/contact.html'
    form_class = ContactForm  # Formulario que se utilizará
    success_url = reverse_lazy('main:home')  # Redirige a esta URL después de enviar el formulario

    def dispatch(self, request, *args, **kwargs):
        # Verifica si el usuario no autenticado ya ha enviado el formulario
        if not request.user.is_authenticated and request.session.get('form_submitted', False):
            messages.error(self.request, _('Ya has enviado un mensaje. Nos pondremos en contacto contigo pronto.'))
            return redirect('main:home')  # Redirige al formulario en lugar de renderizar con un objeto inexistente
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # Guardar el formulario en la base de datos
        form.save()
        # Marcar en la sesión que el formulario ha sido enviado
        if not self.request.user.is_authenticated:
            self.request.session['form_submitted'] = True
        # Mostrar un mensaje de éxito
        messages.success(self.request, _('Tu mensaje ha sido enviado con éxito.\n Nos pondremos en contacto contigo lo antes posible.'))
        # Llamar a la implementación base para completar la validación
        return super().form_valid(form)