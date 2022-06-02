from brain_games import cli


ROUNDS = 3


def engine(description, game_name):
    user_name = cli.welcome_user()
    print(description)
    for i in range(1, ROUNDS + 1):
        question, answer = game_name()
        user_answer = cli.get_answer(question)
        if user_answer != answer:
            print(f"Answer '{user_answer}' is wrong answer ;(.", end=' ')
            print(f" Correct answer was '{answer}'.")
            print(f"Let's try again, {user_name}!")
            break
        else:
            print("Correct!")
            if i == ROUNDS:
                print(f"Congratulations, {user_name}!")
