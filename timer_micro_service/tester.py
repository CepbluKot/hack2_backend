import requests, time

# [{seller_id: time}, ...]
test_data = {}
test_data[1,1] = {"begin_time": time.time(), "duration": 3 }
test_data[1,2] = {"begin_time": time.time(), "duration": 6}
test_data[2,1] = {"begin_time": time.time(), "duration": 7 }
test_data[3,2] = {"begin_time": time.time(), "duration": 8 }
# test_data = 'lol'

rema = {"seller_id": 1, "session_id": 1}

requests.post('http://192.168.227.137:65530/set_timer', json=str(test_data))
requests.post('http://192.168.227.137:65530/remove_timer', json=(rema))
print('done')