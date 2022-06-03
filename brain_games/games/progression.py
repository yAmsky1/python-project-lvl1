from random import randint, choice


DESCRIPTION = 'What number is missing in the progression?'
MAX_VALUE = 10
MIN_VALUE = 0
MAX_DIFF = 10
MIN_DIFF = 1
MIN_LEN = 5
MAX_LEN = 15


def generate_round():
    """
    Brain-progression game.
    -generates first element of a.progression.
    -generates diff of a.progression.
    -generates progression with random length.
    -selects a random element of a.progression (correct answer)
    -replaces the selected element with '..' (generates question)

    returns question and correct answer.
    """
    start = randint(MIN_DIFF, MAX_DIFF)
    diff = randint(MIN_VALUE, MAX_VALUE)
    prog = [str(start + diff * i) for i in range(randint(MIN_LEN, MAX_LEN))]
    answer = choice(prog)
    question = ' '.join(prog).replace(answer, '..', 1)
    return question, answer
