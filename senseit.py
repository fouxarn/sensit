from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import string

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

@app.route("/update", methods=['GET', 'POST'])
def update():
    p = Plate.query.get(request.form['plate_id'])
    if p.weight != request.form['weight']:
        p.weight = request.form['weight']
        db.session.commit()
        update_plate(p.id)
    return ("Hej")

from SMHIData import getSMHIdata
from PakeringsData import getPakeringLkpgdata

def smhi():
    send_mail(getSMHIdata("19:00:00")['t'])
    print(getSMHIdata("19:00:00")['t'])

def parkering():
    return 
    #print(getPakeringLkpgdata("timestring"))

def evaluate_solution(solution):
    switcher = {
        'Send weather report': smhi,
        'Find parking': parkering,
    }

    func = switcher.get(solution.name, lambda: "nothing")
    return func()

def send_mail(text):
    msg = Message('Notifiering',
	       sender='you@dgoogle.com',
	       recipients=['dsjovall@gmail.com'])
    msg.body = text
    mail.send(msg)

def evaluate_function(function):
    function = function.split(" ")
    weight = Plate.query.get(function[0]).weight
    return eval(str(weight) + function[1] + function[2])

def update_plate(plate_id):
    functions = Plate.query.get(plate_id).functions
    for function in functions:
        if evaluate_function(function.regex):
            for solution in function.solutions:
                evaluate_solution(solution)

if __name__ == "__main__":
    app.run('0.0.0.0')
