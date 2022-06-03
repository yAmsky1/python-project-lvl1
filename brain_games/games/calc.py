from operator import sub, mul, add
from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'
MAX_VALUE = 10
MIN_VALUE = 0


def generate_round():
    """
    Brain-calc game.
    -generates two random integers.
    -selects a random math operation from the collection.
    -generates a question for the player.
    -generates correct answer (make math operation on the given numbers).

    returns the question and the correct answer.
    """
    a = randint(MIN_VALUE, MAX_VALUE)
    b = randint(MIN_VALUE, MAX_VALUE)
    operators = {'+': add(a, b), '-': sub(a, b), '*': mul(a, b)}
    operator = choice(list(operators.keys()))
    question = f"{a} {operator} {b}"
    answer = str(operators.get(operator))
    return question, answer
