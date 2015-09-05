from models import *
from SMHIData import getSMHIdata
from ParkeringsData import getParkeringLkpgdata

def smhi():
    print(getSMHIdata("17:00:00"))

def parkering():
    print(getPakeringLkpgdata("timestring"))

def evaluate_solution(solution):
    switcher = {
        'SMHI': smhi,
        'PARK': parkering,
    }

    func = switcher.get(solution.name, lambda: "nothing")
    return func()
