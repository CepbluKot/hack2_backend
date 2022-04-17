# send query if time's over

import time
from storages.time_storages import seller_timers


def check_is_timer_end():
    # ended_timer format: [ended_timer_company_id, ...]
    
    ended_timers = []
    if seller_timers:
        for selected_seller_id in seller_timers:
            if seller_timers[selected_seller_id]["begin_time"] != -1 and time.time() - seller_timers[selected_seller_id]["begin_time"] >= seller_timers[selected_seller_id]["duration"]:
                print('\n\nyeah ', seller_timers[selected_seller_id])
                ended_timers.append(selected_seller_id)

    return ended_timers
