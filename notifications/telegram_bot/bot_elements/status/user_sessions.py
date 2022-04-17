from aiogram import Dispatcher, types
from bot_elements.getters.get_user_data import get_user_all_sessions_data
from bots import main_bot

from bot_elements.getters.parse_query_data import *


async def get_user_data(message: types.Message):
    # format: [{name, end_time, lows pric, our pric, url}, ...]
    # ses name - \n - curr_lowst_pric - our curr pric - beg_time - curr_end time (mb user params)

    message_text = " Активные котировочные сессии:"

    recieved_data = get_user_all_sessions_data(user_id=message.chat.id)

    for selected_session in recieved_data:
        message_text += "\n Session name: " + get_session_name_from_query(selected_session) + " curr_end_time: " + get_session_time_end_from_query(selected_session) + " CURR_LOWEST_PRICE: " + get_session_lowest_price_from_query(selected_session) + " OUR_PRICE: " + get_session_our_price_from_query(selected_session) + "\n URL: " + get_session_url_from_query(selected_session)

    await main_bot.send_message(chat_id=message.chat.id, text=message_text)


def register_handlers_get_user_sessions(dp: Dispatcher):
    dp.register_message_handler(get_user_data, commands="status", state="*")
    