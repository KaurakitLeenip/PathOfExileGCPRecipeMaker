from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from pullGems import *
from threading import Thread, Event

app = Flask(__name__)
socketio = SocketIO(app)

thread = Thread()
thread_stop_event = Event()
class StatusCheckThread(Thread):
    def __init__(self):
        self.delay = 1
        super(StatusCheckThread, self).__init__()

    def getStatusCheck(self):
        while not thread_stop_event.isSet():
            #query for status i guess
            socketio.emit('newstatus', {'line': "adsfas"}, namespace='/')

    def run(self):
        # self.getStatusCheck()
        pass


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('GemCalcForm.html', option_list=get_leagues())
    # else:
    #     #get the form details and pull gems
    #     sess_id = request.form['POESESSID']
    #     league = request.form['League']
    #     max_num = int(request.form['max_recipe_len'])
    #     res = gems(sess_id, max_num, league, socketio)
    #     return render_template('results.html', output=res)

@socketio.on('form_submit', namespace='/')
def get_message(message):
    print(message)
    sess_id = message['POESESSID']
    league = message['league']
    max_num = int(message['max'])
    res = gems(sess_id, max_num, league, socketio)
    return render_template('results.html', output=res)

@socketio.on('connect', namespace='/')
def test_connect():
    global thread

    if not thread.isAlive():
        thread = StatusCheckThread()
        thread.start()
        socketio.emit('newstatus', {'line': "adsfas"}, namespace='/')

    print('client connected')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')