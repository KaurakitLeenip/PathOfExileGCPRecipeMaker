from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    if request.method == 'GET':
        return render_template('GemCalcForm.html')
    else:
        #get the form details and pull gems
        pass