from operator import sub, mul, add
from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'


def calc_game():
    a, b = randint(0, 10), randint(0, 10)
    operators = {'+': add(a, b), '-': sub(a, b), '*': mul(a, b)}
    operator = choice(list(operators.keys()))
    question = f"{a} {operator} {b}"
    answer = str(operators.get(operator))
    return question, answer
