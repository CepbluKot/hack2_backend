from aiogram import Bot
import json

with open('config.json') as file:
    config = json.load(file)

main_bot = Bot(token=config['telegram_bot_token'])
