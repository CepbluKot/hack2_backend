import requests, json, time
from datetime import datetime


data = requests.get(url='http://192.168.227.67:8000/api/qs-history/all/').text
parse = json.loads(data)


for selected_action in parse:
    
    selected_time = selected_action['time']
    selected_time = selected_time.replace("T", "-")
    selected_time = selected_time.replace("Z", "")

    parsed_time = datetime.strptime(selected_time, '%Y-%m-%d-%H:%M:%S.%f')
    time_in_seconds = time.mktime(parsed_time.timetuple())
    

    # print(timez.)
    # print(selected_action['time'])
    # print('\n ', , selected_action['info']['seller']['seller'], selected_action['info']['session']['id'])


# infa = {
#         "id": 2,
#         "time": "23:08:16.821550",
#         "change_cnt": 2,
#         "price": "1400.00",
#         "info": {
#             "id": 2,
#             "auto_status": false,
#             "seller": {
#                 "id": 2,
#                 "password": "pbkdf2_sha256$320000$sLPtARBxk4HcI8AkNm5dxr$+fJQ0jxGOyNwqmI+jPC57xgz8HG26K+TRhTFiqYMcsQ=",
#                 "last_login": null,
#                 "is_superuser": false,
#                 "first_name": "",
#                 "last_name": "",
#                 "is_staff": false,
#                 "is_active": true,
#                 "date_joined": "2022-04-16T22:52:57.677280Z",
#                 "email": "IOEliseev@mai.ru",
#                 "name": "Камаз",
#                 "departure": "Розовый кролик",
#                 "pro": false,
#                 "telegram_id": "",
#                 "seller": {
#                     "id": 2,
#                     "name": "«ДЕТСКАЯ ШКОЛА ИСКУССТВ «ЦЕНТР»"
#                 },
#                 "groups": [],
#                 "user_permissions": []
#             },
#             "session": {
#                 "id": 3,
#                 "name": "ЗАКУПКА ЧЛЕНОВ",
#                 "start_time": "2022-04-16T22:56:24.429712Z",
#                 "end_time": "2022-04-16T22:56:24.429736Z",
#                 "start_price": "90913.00",
#                 "final_price": null,
#                 "reducing_factor": "0.50",
#                 "winner": null
#             }
#         }
#     }

# # requests.post(url='http://192.168.59.67:8000/api/qs-history/all/', json=)
