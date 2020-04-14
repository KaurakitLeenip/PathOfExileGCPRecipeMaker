from flask import Flask, render_template, request
from pullGems import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('GemCalcForm.html', option_list=get_leagues())
    else:
        #get the form details and pull gems
        sess_id = request.form['POESESSID']
        league = request.form['League']
        max_num = int(request.form['max_recipe_len'])
        res = gems(sess_id, max_num, league)
        return render_template('results.html', output=res)