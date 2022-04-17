import requests, json, time
from datetime import datetime

from sqlalchemy import null

from reciever.recv_user_info_from_history import get_user_last_action_info


def send_user_data_to_history(seller_id: int, session_id: int, min_price, auto_status, curr_price):
    data = requests.post(url='http://192.168.227.67:8000/api/qs-history/all/').text

    curr_time_for_django  = '' + str(datetime.date.today() ) + 'T' + str(datetime.datetime.now().time()) + 'Z'
    
    last_id, change_cnt, password, date_joined, seller_name, session_name, start_time, end_time, start_price, final_price, reducing_factor, auto_status = get_user_last_action_info()

    send_data = {
        "id": last_id,
        "time": curr_time_for_django,
        "change_cnt": change_cnt,
        "current_price": str(curr_price),
        "info": {
            "id": session_id,
            "min_price": str(min_price),
            "auto_status": auto_status,
            "seller": {
                "id": seller_id,
                "password": str(password),
                "last_login": null,
                "is_superuser": False,
                "first_name": "",
                "last_name": "",
                "is_staff": False,
                "is_active": True,
                "date_joined": str(date_joined),
                "email": "ivan@mail.ru",
                "name": "Иванов Иван",
                "departament": "Отдел закупок",
                "pro": False,
                "telegram_id": "",
                "seller": {
                    "id": seller_id,
                    "name": str(seller_name)
                },
                "groups": [],
                "user_permissions": []
            },
            "session": {
                "id": session_id,
                "name": str(session_name),
                "start_time": str(start_time),
                "end_time": str(end_time),
                "start_price": str(start_price),
                "final_price": str(final_price),
                "reducing_factor": str(reducing_factor),
                "winner": null
            }
        }
    }

    

    return False
