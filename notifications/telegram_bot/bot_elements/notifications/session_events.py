from bots import main_bot
from telegram_bot.bot_elements.getters import get_session_data
from telegram_bot.bot_elements.getters.parse_query_data import get_session_our_price_from_query, get_session_lowest_price_from_query, get_session_name_from_query, get_session_time_end_from_query, get_session_time_start_from_query, get_session_url_from_query, get_session_win_price_from_query, get_session_winner_name_from_query


async def send_victory_notification(user_id: int, session_id: int):
# user_id: int, session_id: int, session_name: str, final_price: int, time_start, time_end, url: str
    selected_session = get_session_data(session_id=session_id)
    message_text = " Вы победили: " + "\n"
    
    message_text = " \nСессия " + get_session_name_from_query(selected_session)
    message_text += " \nВаша цена: " + get_session_our_price_from_query(selected_session) 
    message_text += " \nНизшая цена: " + get_session_lowest_price_from_query(selected_session) 
    message_text += " \nПобедитель: " + get_session_winner_name_from_query(selected_session) 
    message_text += " \nВремя начала сессии: " + get_session_time_start_from_query(selected_session) 
    message_text += " \nВремя окончания сессии: " + get_session_time_end_from_query(selected_session) 
    message_text += " \nURL: " + get_session_url_from_query(selected_session) 
    
    main_bot.send_message(chat_id=user_id, text=message_text)


async def send_session_end_notification(user_id: int, session_id: int):
# user_id: int, session_id: int, session_name: str, final_price: int, time_start, time_end, win_price: int, url: str, enemy_name: str
    selected_session = get_session_data(session_id=session_id)
    message_text = " Сессия окончена, вы не выиграли " + "\n"

    message_text = " \nСессия " + get_session_name_from_query(selected_session)
    message_text += " \nВаша цена: " + get_session_our_price_from_query(selected_session) 
    message_text += " \nНизшая цена: " + get_session_lowest_price_from_query(selected_session) 
    message_text += " \nПобедитель: " + get_session_winner_name_from_query(selected_session) 
    message_text += " \nВремя начала сессии: " + get_session_time_start_from_query(selected_session) 
    message_text += " \nВремя окончания сессии: " + get_session_time_end_from_query(selected_session) 
    message_text += " \nURL: " + get_session_url_from_query(selected_session) 
    
    main_bot.send_message(chat_id=user_id, text=message_text)


async def send_our_control_system_changed_price(user_id: int, session_id: int):
# user_id: int, session_id: int, session_name: str, final_price: int, url: str
    message_text = " Наша контрольная система снизила цену: \n" 
    
    selected_session = get_session_data(session_id=session_id)
    
    message_text = " \nСессия: " + get_session_name_from_query(selected_session)
    message_text += " \nВаша цена: " + get_session_our_price_from_query(selected_session) 
    message_text += " \nНизшая цена: " + get_session_lowest_price_from_query(selected_session) 
    message_text += " \nВремя окончания сессии: " + get_session_time_end_from_query(selected_session) 
    message_text += " \nURL: " + get_session_url_from_query(selected_session) 
    
    main_bot.send_message(chat_id=user_id, text=message_text)


async def send_competitor_price_is_lower(user_id: int, session_id: int):
# user_id: int, session_id: int, session_name: str, final_price: int, url: str
    message_text += " Нашу цену перебили:" + "\n"
    
    selected_session = get_session_data(session_id=session_id)
    
    message_text = " \nСессия " + get_session_name_from_query(selected_session)
    message_text += " \nВаша цена: " + get_session_our_price_from_query(selected_session) 
    message_text += " \nНизшая цена: " + get_session_lowest_price_from_query(selected_session) 
    message_text += " \nВремя окончания сессии: " + get_session_time_end_from_query(selected_session) 
    message_text += " \nURL: " + get_session_url_from_query(selected_session) 
    
    main_bot.send_message(chat_id=user_id, text=message_text)


async def send_five_min_until_end(user_id: int, session_id: int):
# user_id: int, session_id: int, session_name: str, final_price: int, url: str
    selected_session = get_session_data(session_id=session_id)

    message_text = " До конца сессии осталось 5 минут" + "\n"
    message_text += " \nСессия " + get_session_name_from_query(selected_session)
    message_text += " \nВаша цена: " + get_session_our_price_from_query(selected_session) 
    message_text += " \nНизшая цена: " + get_session_lowest_price_from_query(selected_session) 
    message_text += " \nURL: " + get_session_url_from_query(selected_session) 
    
    main_bot.send_message(chat_id=user_id, text=message_text)


async def session_set_to_manual_mode(user_id: int, session_id: int):
# user_id: int, session_id: int, session_name: str, final_price: int, url: str  
    selected_session = get_session_data(session_id=session_id)
    message_text = " Сессия переведена в ручной режим" + "\n"
    message_text += " \nСессия " + get_session_name_from_query(selected_session)
    message_text += " \nВаша цена: " + get_session_our_price_from_query(selected_session) 
    message_text += " \nНизшая цена: " + get_session_lowest_price_from_query(selected_session) 
    message_text += " \nURL: " + get_session_url_from_query(selected_session) 
