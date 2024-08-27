import requests

# Reemplaza 'TU_BOT_TOKEN' con el token que te dio BotFather
token = '7475987283:AAGhJb3mGkkYNO_j1OJqsBPbQgz46T0yIXw'
url = f'https://api.telegram.org/bot{token}/getUpdates'

response = requests.get(url)
data = response.json()

# Aquí obtendrás toda la información sobre el chat, incluyendo el chat_id
print(data)