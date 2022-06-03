#!/usr/bin/env python


from brain_games.games import even
from brain_games import game_engine


def brain_even():
    game_engine.engine(even)


def main():
    brain_even()


if __name__ == '__main__':
    main()
