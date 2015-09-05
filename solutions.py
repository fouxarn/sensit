from models import *
from SMHIData import getSMHIdata

def smhi():
    print(getSMHIdata("17:00:00"))

def evaluate_solution(solution):
    switcher = {
        'SMHI': smhi,
    }

    func = switcher.get(solution.name, lambda: "nothing")
    return func()
