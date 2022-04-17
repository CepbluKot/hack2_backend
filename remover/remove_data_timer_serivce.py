import json, requests


config = json.loads('config.json')


def remove_timer(remove_this: dict):
    # format  {"seller_id": recieved["seller_id"], "session_id": recieved["session_id"]
    requests.post(config['time_service_ip'] + '/remove_timer', json=remove_this)
