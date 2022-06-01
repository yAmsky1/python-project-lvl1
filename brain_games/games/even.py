from random import randint


def even():
    question = randint(0, 100)
    answer = "yes" if question % 2 == 0 else "no"
    return question, answer
