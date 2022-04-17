# format: [{"address": address, 'subject' : text, "message_text": text}, ...]
def get_user_email_address(message: dict):
    return message["address"]


def get_email_message_text(message: dict):
    return message["message_text"]


def get_email_message_subject(message: dict):
    return message["subject"]
