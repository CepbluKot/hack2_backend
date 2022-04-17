import requests, json, time
from datetime import datetime


def get_all_user_data_from_history():
    data = requests.get(url='http://192.168.227.67:8000/api/qs-history/all/').text
    parse = json.loads(data)

    all_data = []

    for selected_action in parse:
        
        selected_time = selected_action['time']
        selected_time = selected_time.replace("T", "-")
        selected_time = selected_time.replace("Z", "")
        parsed_time = datetime.strptime(selected_time, '%Y-%m-%d-%H:%M:%S.%f')
        time_in_seconds = time.mktime(parsed_time.timetuple())

        auto_status = selected_action['info']["auto_status"]
        begin_time = time_in_seconds
        seller_id = selected_action['info']['seller']['id']
        session_id = selected_action['info']['session']['id']
        min_price_config = selected_action['info']["min_price"]
        current_price = selected_action['current_price']

        all_data.append({"auto_status": auto_status, "begin_time": begin_time, "seller_id": seller_id, "session_id": session_id, "min_price_config": min_price_config, "current_price": current_price})

    return all_data
        

# print('\n ', selected_action['info']["auto_status"], selected_action['info']['session']['id'])


def check_user_in_history(seller_id: int, session_id: int):
    data = requests.get(url='http://192.168.227.67:8000/api/qs-history/all/').text
    parse = json.loads(data)
    parse = parse[::-1]

    for selected_action in parse:
        if selected_action["info"]["session"] == session_id and selected_action["info"]["seller"]["id"] == seller_id:
            return selected_action

    return False


def check_is_user_is_last(seller_id: int, session_id: int):
    data = requests.get(url='http://192.168.227.67:8000/api/qs-history/all/').text
    parse = json.loads(data)

    for selected_action in parse:
        if selected_action["info"]["session"] == session_id and selected_action["info"]["seller"]["id"] == seller_id:
            # selected action = user action
            if selected_action == parse[-1]:
                return True
    
    return False


def get_user_last_action_info():
    data = check_user_in_history()
    if data:
        last_id = data['id']
        change_cnt = data['change_cnt']
        password = data['info']['seller']['password']
        date_joined = data['info']['seller']['date_joined']
        seller_name = data['info']['seller']['seller']['name']
        session_name = data['info']['session']['name']
        start_time = data['info']['session']['start_time']
        end_time = data['info']['session']['end_time']
        start_price = data['info']['session']['start_price']
        final_price = data['info']['session']['final_price']
        reducing_factor = data['info']['session']['reducing_factor']
        auto_status = data['info']['auto_status']

        return last_id, change_cnt, password, date_joined, seller_name, session_name, start_time, end_time, start_price, final_price, reducing_factor, auto_status
