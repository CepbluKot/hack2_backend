import asyncio
from .bots import main_bot


def send_telegram_notification(user_id: int, text: str):
    
    asyncio.run(main_bot.send_message(chat_id=user_id, text=text))
