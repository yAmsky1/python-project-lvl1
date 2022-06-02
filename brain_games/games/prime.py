from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime_game():
    question = randint(0, 100)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer


def is_prime(number):
    if number == 0:
        return False
    for den in range(2, number):
        if number % den == 0:
            return False
    return True
