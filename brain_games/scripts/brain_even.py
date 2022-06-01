#!/usr/bin/env python


from brain_games import cli
from random import randint
import prompt


ROUNDS = 3


def brain_even():
    user_name = cli.welcome_user()
    print('Answer "yes" if  the number is even, otherwise answer "no".')
    for i in range(1, ROUNDS + 1):
        question = randint(0, 100)
        answer = "yes" if question % 2 == 0 else "no"
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')
        if user_answer != answer:
            print(f"Answer '{user_answer}' is wrong answer ;(.", end=' ')
            print(f" Correct answer was '{answer}'.")
            print(f"Let's try again, {user_name}!")
            break
        else:
            print("Correct!")
            if i == ROUNDS:
                print(f"Congratulations, {user_name}!")


def main():
    brain_even()


if __name__ == '__main__':
    main()
