from senseit import db

class Plate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    weight = db.Column(db.Float)

    def __init__(self, name):
        self.name = name
        self.weight = 0

class Plate_Trigger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plate_id = db.Column(db.Integer, db.ForeignKey('plate.id'))
    function_id = db.Column(db.Integer, db.ForeignKey('function.id'))

    def __init__(self, plate_id, function_id):
        self.plate_id = plate_id
        self.function_id = function_id

class Function(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    regex = db.Column(db.String(80))

    def __init__(self, regex):
        self.regex = regex

class Solution_Trigger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    solution_id = db.Column(db.Integer, db.ForeignKey('solution.id'))
    function_id = db.Column(db.Integer, db.ForeignKey('function.id'))

    def __init__(self, solution_id, function_id):
        self.solution_id = solution_id
        self.function_id = function_id

class Solution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)

    def __init__(self, name):
        self.name = name
