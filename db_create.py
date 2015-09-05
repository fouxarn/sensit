from senseit import db
from models import *

db.drop_all()
db.create_all()

p1 = Plate('Kök')
f1 = Function('If this then that')
p1.functions.append(f1)
db.session.add(p1)
db.session.commit()
