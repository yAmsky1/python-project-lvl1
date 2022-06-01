#!/usr/bin/env python


from brain_games.games import progression
from brain_games import cli, game_engine


def brain_progression():
    user_name = cli.welcome_user()
    print('What number is missing in the progression?')
    game_engine.game_engine(progression.progression, user_name)


def main():
    brain_progression()


if __name__ == '__main__':
    main()
