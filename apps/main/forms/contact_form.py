from django import forms
from ..models import Contact
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.ModelForm):
    SERVICE_CHOICES = [
        ('', _('Elige el Servicio')),
        ('ecommerce', _('Desarrollo de eCommerce')),
        ('marketplace', _('Desarrollo de Marketplace')),
        ('erp-crm', _('Desarrollo de ERP y CRM')),
        ('ai-integration', _('Integraciones de IA')),
    ]
    
    service = forms.ChoiceField(
        choices=SERVICE_CHOICES,
        widget=forms.Select(attrs={'class': 'tj-nice-select'}),
        required=True,
        label=_('Servicio'),
    )

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'service', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': _('Nombre')}),
            'last_name': forms.TextInput(attrs={'placeholder': _('Apellido')}),
            'email': forms.EmailInput(attrs={'placeholder': _('Correo Electrónico')}),
            'phone': forms.TextInput(attrs={'placeholder': _('Número de Teléfono')}),
            'message': forms.Textarea(attrs={'placeholder': _('Mensaje')}),
        }