import threading, json
import ast
from flask import Flask, request, jsonify
from flask_cors import CORS
from setters.set_recieved_time import set_recieved_time
from timer_procedures.timer_checker import check_is_timer_end
from remover.remover import remove_seller


app = Flask(__name__)


port = 65530
url = "http://localhost:" + str(port)
cors = CORS(app, resources={r"/*": {"origins": url}})


@app.before_first_request
def light_thread():
    def notifier():
        
        while True:
            
            ended_timers = check_is_timer_end()
    
            if ended_timers:
                print('\n\n\n wow ', ended_timers,'\n\n')
                for selected_seller_id in ended_timers:
                    print('\n\n posting ', selected_seller_id)
                    # requests.post('http://10.10.117.207:65530/test', json=selected_seller_id)
                    remove_seller(seller_id=selected_seller_id)
            

    thread = threading.Thread(target=notifier)
    thread.daemon = True
    thread.start()


@app.route("/set_timer", methods=["POST"])
def reciever():
    if request.method == "POST":
        # format: [{(seller id, session_id): {"time": time, "duration": duration}}, ...]
        # recieves time as time.time (seconds)

        recieved = request.json
        recieved = ast.literal_eval(recieved)
        print(recieved)

        print('\n\n', recieved)
        
        for selected_user_id in recieved:
        #selected_user format : {(seller id, session_id): {"begin_time": time, "duration": duration}}
            
            set_recieved_time(seller_id=selected_user_id[0], session_id=selected_user_id[1], timer_new_time=recieved[selected_user_id]["begin_time"], duration=recieved[selected_user_id]["duration"])
        
        return jsonify(str(recieved))


@app.route("/remove_timer", methods=["POST"])
def removr():
    if request.method == "POST":
        # recieves: {"seller_id": seller_id, "session_id": session_id)

        recieved = (request.json)
        # print('asgarsgdrg\n\n', recieved , recieved["seller_id"], '\n\n')
        remove_seller(seller_id=(recieved["seller_id"], recieved["session_id"]))
        
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
