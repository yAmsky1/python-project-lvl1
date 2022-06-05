from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MAX_VALUE = 100
MIN_VALUE = 0


def generate_round():
    """
    Brain-prime game.
    -generates random integer (question for the player).
    -generates correct answer (result of is_prime func).

    returns the question and the correct answer.
    """
    question = randint(MIN_VALUE, MAX_VALUE)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer


def is_prime(number):
    if number == 0 or number == 1:
        return False
    for den in range(2, (number // 2) + 1):
        if number % den == 0:
            return False
    return True
