from random import randint, choice


def progression():
    a0, d = randint(0, 10), randint(1, 10)  # a0 - first element, d - diff
    prog = [str(a0 + d * i) for i in range(randint(5, 16))]
    answer = choice(prog)
    question = ' '.join(prog).replace(answer, '..', 1)
    return question, answer
