from flask import Flask, render_template, request, abort
from flask_socketio import SocketIO, emit
from pullGems import *
from threading import Thread, Event
from websocket import get_status_message
from time import sleep

app = Flask(__name__)
socketio = SocketIO(app)

thread = None
thread_stop_event = Event()
# class StatusCheckThread(Thread):
#     def __init__(self):
#         self.delay = 1
#         super(StatusCheckThread, self).__init__()
#
#     def getStatusCheck(self):
#         while not thread_stop_event.isSet():
#             #query for status i guess
#             status = get_status_message()
#             if status != "":
#                 socketio.emit('newstatus', {'line': status}, namespace='/')
#
#     def run(self):
#         self.getStatusCheck()
#         sleep(2)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('GemCalcForm.html', option_list=get_leagues())
    if request.method == 'POST':
        sess_id = request.form['POESESSID']
        league = request.form['League']
        max_num = int(request.form['max_recipe_len'])
        global thread
        try:
            thread = PullGemsThread(sess_id, max_num, league)
            thread.start()
            return render_template('results.html', output=thread.results)
        except ValueError:
            # poe api is rate limiting you
            abort(429)

@app.route("/set_progress/", methods=['GET'])
def get_prog():
    global thread
    if thread.isAlive():
        print(thread.status_message)
        status = thread.status_message
        return str(status)
    else:
        return str(thread.results)


@socketio.on('form_submit', namespace='/')
def get_message(message):
    #get form and pull gems
    print(message)
    sess_id = message['POESESSID']
    league = message['league']
    max_num = int(message['max'])
    global thread
    thread = PullGemsThread(sess_id, max_num, league)
    thread.start()
    thread.join()
    thread = None

# @socketio.on('get_status')
# def set_message():
#     global thread
#     if thread:
#         print(thread.status_message)
#         status = thread.status_message
#         socketio.emit('newstatus', {'line': status}, namespace='/')


@socketio.on('connect', namespace='/')
def test_connect():

    print('client connected')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')