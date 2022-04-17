import requests


def send_telegram_notification(send_data):
    # [{"user_id": user_id, "message_text": text}, ...]
    requests.post(url='http://192.168.227.137:65510/send_telegram_notification', json=send_data)

def send_email_notification(send_data):
    # [{"address": address, "message_text": text, "subject": text}, ...]
    requests.post(url='http://192.168.227.137:65510/send_email_notification', json=send_data)

