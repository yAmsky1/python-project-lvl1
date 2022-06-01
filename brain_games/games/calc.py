from operator import sub, mul, add
from random import randint, choice


def calc():
    a, b = randint(0, 10), randint(0, 10)
    operators = {'+': add(a, b), '-': sub(a, b), '*': mul(a, b)}
    operator = choice(list(operators.keys()))
    question = f"{a} {operator} {b}"
    answer = operators.get(operator)
    return question, str(answer)
