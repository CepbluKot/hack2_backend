from aiogram import Dispatcher, types
from bot_elements.getters.get_notification_status import get_user_notification_status
from bot_elements.sender.change_recieve_notify import user_turn_off_notify, user_turn_on_notify


async def change_recieve_notify_status(message: types.Message):
    message_text = "Уведомления: "
    
    current_notify_status = get_user_notification_status(user_id=message.chat.id)
    
    if current_notify_status:
        message_text += "включены"
    
    else:
        message_text += "выключены"

    buttons_turn_notify_on = [
        types.InlineKeyboardButton(
            text="Включить", callback_data="change_notifications_turn_on"),
        types.InlineKeyboardButton(
            text="Не изменять", callback_data="change_notifications_do_nothing"), 
    ]

    buttons_turn_notify_off = [
        types.InlineKeyboardButton(
            text="Выключить", callback_data="change_notifications_turn_off"),
        types.InlineKeyboardButton(
            text="Не изменять", callback_data="change_notifications_do_nothing"), 
    ]

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    await message.reply(text=message_text)

    if current_notify_status:
        keyboard.add(*buttons_turn_notify_off)
        await message.reply(text="Изменить статус уведомлений?", reply_markup=keyboard)

    else:
        keyboard.add(*buttons_turn_notify_on)
        await message.reply(text="Изменить статус уведомлений?", reply_markup=keyboard)


async def change_notifications_turn_on(call: types.CallbackQuery):
    await call.answer()
    await types.Message.edit_reply_markup(self=call.message, reply_markup=None)

    user_turn_on_notify(user_id=call.from_user.id)
    await call.message.answer("Уведомления включены")


async def change_notifications_turn_off(call: types.CallbackQuery):
    await call.answer()
    await types.Message.edit_reply_markup(self=call.message, reply_markup=None)
    
    user_turn_off_notify(user_id=call.from_user.id)
    await call.message.answer("Уведомления отключены")


async def change_notify_do_nothing(call: types.CallbackQuery):
    await call.answer()
    await types.Message.edit_reply_markup(self=call.message, reply_markup=None)

    await call.message.answer("Статус уведомлений не изменен")


def register_handlers_notifications(dp: Dispatcher):
    dp.register_message_handler(change_recieve_notify_status, commands="config_notifications", state="*")
    dp.register_callback_query_handler(change_notifications_turn_on, text="change_notifications_turn_on")
    dp.register_callback_query_handler(change_notifications_turn_off, text="change_notifications_turn_off")
    dp.register_callback_query_handler(change_notify_do_nothing, text="change_notifications_do_nothing")
    