from senseit import db
from models import *

db.drop_all()
db.create_all()

p1 = Plate('Mjölksensor', 'Kök')
p2 = Plate('TVsensor', 'Vardagsrum')
p3 = Plate('Toalettsensor', 'Badrum')
p4 = Plate('Oboysensor', 'Kök')
f1 = Function('Gå upp ur säng', '1 < 50')
s1 = Solution('SMHI')
p1.functions.append(f1)
f1.solutions.append(s1)
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)
db.session.commit()
