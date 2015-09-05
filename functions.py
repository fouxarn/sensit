from models import *
from solutions import evaluate_solution
import string

def evaluate_function(function):
    function = function.split(" ")
    weight = Plate.query.get(function[0]).weight
    return eval(str(weight) + function[1] + function[2])

def update(plate_id):
    functions = Plate.query.get(plate_id).functions
    for function in functions:
        if evaluate_function(function.regex):
            for solution in function.solutions:
                evaluate_solution(solution)
