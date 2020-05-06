from flask import Flask, render_template, request, abort
from pullGems import *
from jinja2 import Environment, FileSystemLoader, select_autoescape

app = Flask(__name__)

thread = None

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
    if not thread:
        return ""
    if thread.isAlive():
        if thread.results:
            return str('DONE')
        status = thread.status_message
        return str(status)

    else:
        return str('DONE')

@app.route("/results", methods=['GET'])
def get_results():
    global thread
    if thread:
        if thread.results:
            results = thread.results
            template_loader = FileSystemLoader(searchpath="./")
            templateEnv = Environment(
                loader=template_loader, autoescape=select_autoescape(['html', 'xml']))
            template_file = "/templates/results.html"
            template = templateEnv.get_template(template_file)
            output = template.render(output=results, remainder=thread.remainder, recipes=thread.recipes)
            print(output)
            return output
    abort(404)


if __name__ == '__main__':
    Flask.run(app, host='0.0.0.0')