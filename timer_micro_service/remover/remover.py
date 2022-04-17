from storages.time_storages import seller_timers


def remove_seller(seller_id):
    if seller_id in seller_timers.keys():
        seller_timers[seller_id] = {"begin_time": -1, "duration": 0}
        print('\n\nai removd', seller_id)
