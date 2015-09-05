from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
from models import *

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        p = Plate.query.get(request.form['plate_id'])
        f = Function(request.form['function'])
        p.functions.append(f)
    functions = Function.query.all()
    return render_template('index.html', functions=functions)

@app.route("/sensors")
def sensor():
    plates = Plate.query.all()
    return render_template('sensors.html', plates=plates)

@app.route("/stats")
def stats():
    return render_template('stats.html')

if __name__ == "__main__":
    app.run()
