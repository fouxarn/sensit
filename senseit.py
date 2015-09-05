from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
from models import *

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = Function.query.get(request.form['function_id'])
        s = Solution.query.get(request.form['solution_id'])
        f.solutions.append(s)
        db.session.add(f)
        db.session.commit()
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
