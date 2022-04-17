from storages.time_storages import seller_timers


def get_seller_time(seller_id: int):

    return seller_timers[seller_id]
