from random import randint


DESCRIPTION = 'Answer "yes" if  the number is even, otherwise answer "no".'


def even_game():
    question = randint(0, 100)
    answer = "yes" if question % 2 == 0 else "no"
    return question, answer
