from telegram_bot.send_notification import send_telegram_notification
from mail.send import send_email


send_telegram_notification(user_id=506629389, text='test messeg')
send_email('igmalysch@yandex.ru', "thi si ef", "test messeg")
