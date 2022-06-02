from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd_game():
    a, b = randint(0, 10), randint(0, 10)
    question = f"{a} {b}"
    answer = str(get_gcd(a, b))
    return question, answer


def get_gcd(a, b):
    if b == 0:
        return a
    else:
        return get_gcd(b, a % b)
