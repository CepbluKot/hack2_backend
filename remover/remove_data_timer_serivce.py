import json, requests


# config = json.loads('config.json')


def remove_timer(remove_this: dict):
    # format  {"seller_id": recieved["seller_id"], "session_id": recieved["session_id"]
    requests.post('http://192.168.227.137:65530' + '/remove_timer', json=remove_this)
