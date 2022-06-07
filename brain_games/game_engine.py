import prompt


ROUNDS_COUNT = 3


def engine(game):
    user_name = welcome_user()
    print(game.DESCRIPTION)
    for i in range(ROUNDS_COUNT):
        question, answer = game.generate_round()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')
        if user_answer != answer:
            print(f"Answer '{user_answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{answer}'.")
            print(f"Let's try again, {user_name}!")
            return
        else:
            print("Correct!")
    print(f"Congratulations, {user_name}!")


def welcome_user():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")
    return user_name
