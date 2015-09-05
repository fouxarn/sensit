from senseit import db

plate_trigger = db.Table('plate_trigger',
    db.Column('plate_id', db.Integer, db.ForeignKey('plate.id')),
    db.Column('function_id', db.Integer, db.ForeignKey('function.id'))
)

solution_trigger = db.Table('solution_trigger',
    db.Column('solution_id', db.Integer, db.ForeignKey('solution.id')),
    db.Column('function_id', db.Integer, db.ForeignKey('function.id'))
)

class Plate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    place = db.Column(db.String(30))
    weight = db.Column(db.Float)
    functions = db.relationship('Function', secondary=plate_trigger,
        backref=db.backref('plates', lazy='dynamic'))

    def __init__(self, name, place):
        self.name = name
        self.place = place
        self.weight = 0

    def __repr__(self):
        return '{} {} {} {}'.format(self.id, self.name, self.place, self.weight)

class Function(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    regex = db.Column(db.String(80))
    solutions = db.relationship('Solution', secondary=solution_trigger,
        backref=db.backref('functions', lazy='dynamic'))

    def __init__(self, regex):
        self.regex = regex

    def __repr__(self):
        return '{} {}'.format(self.id, self.regex)

class Solution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '{} {}'.format(self.id, self.name)
