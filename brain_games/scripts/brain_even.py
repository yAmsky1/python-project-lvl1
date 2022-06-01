#!/usr/bin/env python


from brain_games.games import even
from brain_games import cli, game_engine


def brain_even():
    user_name = cli.welcome_user()
    print('Answer "yes" if  the number is even, otherwise answer "no".')
    game_engine.game_engine(even.even, user_name)


def main():
    brain_even()


if __name__ == '__main__':
    main()
