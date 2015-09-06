from models import *
from SMHIData import getSMHIdata
from ParkeringsData import getParkeringLkpgdata
from senseit import send_mail

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
