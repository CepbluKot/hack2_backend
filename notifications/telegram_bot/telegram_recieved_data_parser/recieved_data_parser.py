# format: [{"user_id": user_id, "message_text": text}, ...]
def get_user_id(message: dict):
    return message["user_id"]


def get_telegram_message_text(message: dict):
    return message["message_text"]
