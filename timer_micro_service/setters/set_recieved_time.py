from storages.time_storages import seller_timers


def set_recieved_time(seller_id: int, timer_new_time, session_id: int, duration):
    
    seller_timers[seller_id, session_id] = {"begin_time": timer_new_time, "duration": duration}
