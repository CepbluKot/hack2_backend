import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bots import main_bot
from bot_elements.notifications.notifications_menu import register_handlers_notifications
from bot_elements.status.user_sessions import register_handlers_get_user_sessions

async def bot_commands(bot: Bot):
    bot_commands = [
        # BotCommand(command="/config_notifications", description="Получать уведомления?"),
        BotCommand(command="/status", description="Получить инфу обо всех активных сессиях")
    ]
    await bot.set_my_commands(bot_commands)


async def main():
    main_bot_dispatcher = Dispatcher(main_bot, storage=MemoryStorage(),
                    loop=asyncio.get_event_loop())
    main_bot_dispatcher.loop.create_task(bot_commands(main_bot))
    register_handlers_notifications(main_bot_dispatcher)
    register_handlers_get_user_sessions(main_bot_dispatcher)
    
    await main_bot_dispatcher.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
    