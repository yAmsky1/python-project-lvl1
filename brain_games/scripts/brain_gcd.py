#!/usr/bin/env python


from brain_games.games import gcd
from brain_games import cli, game_engine


def brain_gcd():
    user_name = cli.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    game_engine.game_engine(gcd.gcd, user_name)


def main():
    brain_gcd()


if __name__ == '__main__':
    main()
