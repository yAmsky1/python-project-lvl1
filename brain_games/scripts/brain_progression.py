#!/usr/bin/env python


from brain_games.games import progression
from brain_games import game_engine


def brain_progression():
    game_engine.engine(progression)


def main():
    brain_progression()


if __name__ == '__main__':
    main()
