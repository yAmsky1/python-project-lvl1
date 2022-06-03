from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MAX_VALUE = 100
MIN_VALUE = 0


def generate_round():
    """
    Brain-gcd game.
    -generates two random integers.
    -generates a question for the player.
    -generates correct answer (result of get_gcd func).

    returns the question and the correct answer.
    """
    a = randint(MIN_VALUE, MAX_VALUE)
    b = randint(MIN_VALUE, MAX_VALUE)
    question = f"{a} {b}"
    answer = str(get_gcd(a, b))
    return question, answer


def get_gcd(a, b):
    """
    Searching the greatest common divisor for two integers
    """
    if b == 0:
        return a
    else:
        return get_gcd(b, a % b)
