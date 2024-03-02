from json import load

with open('config.json') as file:
    config = load(file)

TOKEN = config.get('token')
CHAT_ID = config.get('chat_id')
BOT_ID = config.get('bot_id')