from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
mail = Mail(app)
from models import *

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['method'] == 'ADD':
            f = Function.query.get(request.form['function_id'])
            s = Solution.query.get(request.form['solution_id'])
            f.solutions.append(s)
            db.session.add(f)
            db.session.commit()
        elif request.form['method'] == 'DELETE':
            function = Function.query.get(request.form['function_id'])
            for solution in function.solutions:
                function.solutions.remove(solution)
            db.session.commit()

    functions = Function.query.all()
    solutions = Solution.query.all()
    return render_template('index.html', functions=functions, solutions=solutions)

@app.route("/sensors")
def sensor():
    plates = Plate.query.all()
    return render_template('sensors.html', plates=plates)

@app.route("/stats")
def stats():
    return render_template('stats.html')

@app.route("/functions")
def functions():
    functions = Function.query.all()
    plates = Plate.query.all()
    for function in functions:
        temp = function.regex.split(" ")
        function.sensor = temp[0]
        function.operator = temp[1]
        function.weight = temp[2]
    return render_template('functions.html', plates=plates, functions=functions)

@app.route("/update", methods=['POST'])
def update():
    p = Plate.query.get(request.form['plate_id'])
    p.weight = request.form['weight']
    db.session.commit()
    update(p.id)

def send_mail(text):
    msg = Message('Notifiering',
	       sender='you@dgoogle.com',
	       recipients=['dsjovall@gmail.com'])
    msg.body = text
    mail.send(msg)

if __name__ == "__main__":
    app.run('0.0.0.0')
