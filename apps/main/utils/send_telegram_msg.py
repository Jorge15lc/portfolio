import requests
from django.conf import settings

def send_telegram_notification(contact_data):
    """
    Envía un mensaje a través de un bot de Telegram cuando se envía un formulario de contacto.

    :param contact_data: Un diccionario con los datos de contacto del formulario.
    """
    
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID
    message = (
        f"Nuevo mensaje de contacto:\n\n"
        f"Nombre: {contact_data['first_name']} {contact_data['last_name']}\n"
        f"Email: {contact_data['email']}\n"
        f"Teléfono: {contact_data['phone']}\n"
        f"Servicio: {contact_data['service']}\n"
        f"Mensaje:\n{contact_data['message']}\n"
    )
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {'chat_id': chat_id, 'text': message}
    response = requests.post(url, data=data)
    
    if response.status_code != 200:
        # Maneja posibles errores en el envío
        raise Exception(f"Error al enviar mensaje a Telegram: {response.status_code}, {response.text}")