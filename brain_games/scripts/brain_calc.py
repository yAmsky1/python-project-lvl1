#!/usr/bin/env python


from brain_games.games import calc
from brain_games import game_engine


def brain_calc():
    game_engine.engine(calc.DESCRIPTION, calc.calc_game)


def main():
    brain_calc()


if __name__ == '__main__':
    main()
