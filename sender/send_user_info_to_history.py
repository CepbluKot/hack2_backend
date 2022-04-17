import requests, json, time
from datetime import datetime

from sqlalchemy import null

from reciever.recv_user_info_from_history import get_user_last_action_info


def send_user_data_to_history(curr_price):
    # data = requests.get(url='http://192.168.227.67:8000/api/qs-history/all/').text

    send_data = {
        
        "current_price": curr_price,
        "info": 1,
        
    }

    # requests.post(url='http://192.168.227.67:8000/api/qs-history/insert/', json=send_data)
    print('\n\n ', send_data ,' \n\n')
