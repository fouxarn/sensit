from senseit import db
from models import *

db.drop_all()
db.create_all()

p1 = Plate('Milk', 'Kitchen')
p2 = Plate('TVsensor', 'Vardagsrum')
p3 = Plate('Car', 'Driveway')
p4 = Plate('Bed', 'Bedroom')
f1 = Function('Leave bed', '4 < 50', 'images/bed.png')
f2 = Function('Milk empty', '1 < 0.5', 'images/milk.png')
f3 = Function('Car leaving', '3 < 1000', 'images/car.png')
f4 = Function('In bed', '4 > 50', 'images/bed.png')
f5 = Function('Milk full', '1 > 0.5', 'images/milk.png')
f6 = Function('Car arriving', '3 > 1000', 'images/car.png')
s1 = Solution('SMHI', 'images/weather.png')
s2 = Solution('PARK', 'images/parking.png')
p1.functions.append(f1)
p2.functions.append(f2)
f1.solutions.append(s1)
f1.solutions.append(s2)
f2.solutions.append(s1)
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)
db.session.add(f3)
db.session.add(f4)
db.session.add(f5)
db.session.add(f6)
db.session.commit()
