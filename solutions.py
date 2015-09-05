from models import *

def smhi():
    return

def evaluate_solution(solution):
    switcher {
        'SMHI': smhi,
    }

    func = switcher.get(solution.name, lambda: "nothing")
    return func()
