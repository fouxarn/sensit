from models import *
from SMHIData import getSMHIdata
from PakeringsData import getPakeringLkpgdata
from senseit import mail

def smhi():
    send_mail(getSMHIdata("17:00:00"))
    print(getSMHIdata("17:00:00"))

def parkering():
    print(getPakeringLkpgdata("timestring"))

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
