import threading, time, requests, json
import ast
from flask import Flask, request, jsonify
from flask_cors import CORS
from reciever.recv_user_info_from_history import check_is_user_is_last, get_all_user_data_from_history
from sender.send_to_time_service import send_data_to_time_service
from remover.remove_data_timer_serivce import remove_timer
from sender.send_user_info_to_history import send_user_data_to_history
# todo 
# autoa
# add user to timr
# check his min price from his config
# if last input isn his one (seller id)

# hes new price set to new price
# send to histori
# save previoss best bet (id)
# is auto is enabl
# true = create new timer and creat new timr (step 1) and del old
# false do nothin
# new winner notify hes cool
# notify last winnder he sucks

# manual 
# check isnt hes last
# if auto = enable
# true delete his prev timer
# and to prv bloack


app = Flask(__name__)


port = 65520
url = "http://localhost:" + str(port)
cors = CORS(app, resources={r"/*": {"origins": url}})


@app.before_first_request
def test():
    def test_timer():
        test_data = {}

        test_data[1,11] = {"begin_time": time.time(), "duration": 5 }
        test_data[1,12] = {"begin_time": time.time(), "duration": 6}
        test_data[21,1] = {"begin_time": time.time(), "duration": 7 }
        test_data[31,2] = {"begin_time": time.time(), "duration": 10}
        # test_data = 'lol'

        send_data_to_time_service(data=test_data)
        print('done')

    thread = threading.Thread(target=test_timer)
    thread.daemon = True
    thread.start()


@app.route("/test", methods=["POST"])
def reciever():
    if request.method == "POST":
        # recieved seller_id and session_id
        recieved = request.json
        print('\n got smth ',recieved)
        return jsonify(str(recieved))

# check is user auto
@app.route("/add_seller_to_session", methods=["POST"])
def reciever():
    if request.method == "POST":
        recieved = request.json
        
        
        # recieved format: {"auto_status": auto_status, "begin_time": begin_time, "seller_id": seller_id, "session_id": session_id, 'new_price': price, 'input_type': auto/manual, 'min_price_config': min_price}
            

            # if recieved['auto_status'] == True:
            # if recieved['input_type'] == 'auto':
            #     if not recieved['new_price'] < checker['info']['min_price']:
                    
            #         data_to_send = {}
            #         data_to_send[recieved["seller_id"], recieved["session_id"]] = {"time": recieved["begin_time"], "duration": recieved["duration"]}
            #         # send data format: str [{(seller id, session_id): {"time": time, "duration": duration}}, ...]
            #         send_data_to_time_service(str(list(data_to_send)))
            #     else:
            #         return jsonify('MIN PRICE ERROR')

            # else:
            #     if not check_is_user_is_last(seller_id=recieved["seller_id"], session_id=recieved["session_id"]):
            #         if recieved['auto_status'] == True:
                        
            #             remove_this = {"seller_id": recieved["seller_id"], "session_id": recieved["session_id"]}
            #             requests.post(config['time_service_ip'] + '/remove_timer', json=remove_this)
                
            #     else:
            #         return jsonify('IS LAST USER ERROR')

        
        if recieved['input_type'] == 'auto':
            if not recieved['new_price'] < recieved['min_price_config']:
                
                data_to_send = {}
                data_to_send[recieved["seller_id"], recieved["session_id"]] = {"time": recieved["begin_time"], "duration": recieved["duration"]}
                # send data format: str [{(seller id, session_id): {"time": time, "duration": duration}}, ...]
                send_data_to_time_service(str(list(data_to_send)))
            else:
                return jsonify('MIN PRICE ERROR')

        else:
            if not check_is_user_is_last(seller_id=recieved["seller_id"], session_id=recieved["seller_id"]):
                if recieved['auto_status'] == True:
                    
                    remove_this = {"seller_id": recieved["seller_id"], "session_id": recieved["session_id"]}
                    remove_timer(remove_this=remove_this)
            else:
                return jsonify('IS LAST USER ERROR')

        send_user_data_to_history(seller_id=recieved["seller_id"],session_id=recieved["seller_id"],min_price=recieved['min_price_config'],auto_status=recieved['auto_status'],curr_price=recieved['new_price'])
        

        # print('\n got smth ',recieved)
        return jsonify(str(recieved))


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "500"})


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "404"})


@app.errorhandler(400)
def not_found(error):
    return jsonify({"error": "400"})


def flask_start():
    app.run('0.0.0.0', port=str(port))


if __name__ == "__main__":
    flask_start()
