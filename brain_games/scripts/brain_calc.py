#!/usr/bin/env python


from brain_games.games import calc
from brain_games import cli, game_engine


def brain_calc():
    user_name = cli.welcome_user()
    print('What is the result of the expression?')
    game_engine.game_engine(calc.calc, user_name)


def main():
    brain_calc()


if __name__ == '__main__':
    main()
