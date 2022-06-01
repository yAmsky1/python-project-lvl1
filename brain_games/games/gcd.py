from random import randint


def gcd():
    a, b = randint(0, 10), randint(0, 10)
    question = f"{a} {b}"
    answer = get_gcd(a, b)
    return question, str(answer)


def get_gcd(a, b):
    if b == 0:
        return a
    else:
        return get_gcd(b, a % b)
