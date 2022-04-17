from flask import Flask, request, jsonify
from flask_cors import CORS
from telegram_bot.telegram_recieved_data_parser.recieved_data_parser import *
from telegram_bot.send_notification import send_telegram_notification

from mail.recieved_data_parser.email_recieved_data_parser import *
from mail.send import send_email

app = Flask(__name__)


port = 65520
url = "http://localhost:" + str(port)
cors = CORS(app, resources={r"/*": {"origins": url}})


@app.route("/send_telegram_notification", methods=["POST"])
def telegram_notify():
    if request.method == "POST":
        # format: [{"user_id": user_id, "message_text": text}, ...]
        
        recieved = request.json
        for selected_element in recieved:
            user_id = get_user_id(selected_element)
            message_text = get_telegram_message_text(selected_element)
            send_telegram_notification(user_id=user_id, text=message_text)

        return jsonify(True)


@app.route("/send_email_notification", methods=["POST"])
def email_notify():
    if request.method == "POST":
        recieved = request.json
        for selected_element in recieved:
            address = get_user_email_address(selected_element)
            message_text = get_email_message_text(selected_element)
            subject = get_email_message_subject(selected_element)

            send_email(to_user_email=address, subject=subject, text=message_text)

        return jsonify(True)


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "500"})


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "404"})


@app.errorhandler(400)
def not_found(error):
    return jsonify({"error": "400"})


def flask_start():
    app.run('0.0.0.0', port=str(port))


if __name__ == "__main__":
    flask_start()
