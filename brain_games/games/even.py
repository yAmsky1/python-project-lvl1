from random import randint


DESCRIPTION = 'Answer "yes" if  the number is even, otherwise answer "no".'
MAX_VALUE = 100
MIN_VALUE = 0


def generate_round():
    """
    Brain-even game.
    -generates random integer (question for the player).
    -generates correct answer.

    returns the question and the correct answer.
    """
    question = randint(MIN_VALUE, MAX_VALUE)
    answer = "yes" if question % 2 == 0 else "no"
    return question, answer
