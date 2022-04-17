import requests
import json
import time


with open('config.json') as file:
    config = json.load(file)


current_time_recvice_ip = config["time_service_ip"]


def send_data_to_time_service(data: dict):
    # send [{(seller id, session_id): {"time": time, "duration": duration}}, ...]
    requests.post(current_time_recvice_ip + '/set_timer', json=str(data))


def delete_timer(seller_id: int, session_id: int):
    # recieves: (seller_id, session_id)
    data = {"seller_id": seller_id, "session_id": session_id}
    requests.post(current_time_recvice_ip + '/set_timer', json=str(data))
