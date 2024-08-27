import requests
from django.conf import settings

# Reemplaza 'TU_BOT_TOKEN' con el token que te dio BotFather
token = settings.TELEGRAM_BOT_TOKEN
url = f'https://api.telegram.org/bot{token}/getUpdates'

response = requests.get(url)
data = response.json()

# Aquí obtendrás toda la información sobre el chat, incluyendo el chat_id
print(data)