from flask import Flask, render_template
from flask import send_from_directory
import os


app = Flask(__name__, static_url_path="")

@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/base/')
def hello():
    return render_template('base.html')

@app.route('/api/wines')
def lol():
    import json
    data = open('./data/wines.json','r')
    data = json.load(data)
    return data

@app.route('/path')
def path():
    return os.getcwd()

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

with app.app_context():
    from .dash_pages.predictor import init_regression
    app = init_regression(app)

if __name__ == '__main__':
    app.run(threaded=True, debug=False)
