from random import randint, choice


DESCRIPTION = 'What number is missing in the progression?'


def progression_game():
    a0, d = randint(0, 10), randint(1, 10)
    prog = [str(a0 + d * i) for i in range(randint(5, 16))]
    answer = choice(prog)
    question = ' '.join(prog).replace(answer, '..', 1)
    return question, answer
