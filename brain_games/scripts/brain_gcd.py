#!/usr/bin/env python


from brain_games.games import gcd
from brain_games import game_engine


def brain_gcd():
    game_engine.engine(gcd)


def main():
    brain_gcd()


if __name__ == '__main__':
    main()
