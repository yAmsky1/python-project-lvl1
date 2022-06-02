#!/usr/bin/env python


from brain_games.games import prime
from brain_games import game_engine


def brain_prime():
    game_engine.engine(prime.DESCRIPTION, prime.prime_game)


def main():
    brain_prime()


if __name__ == '__main__':
    main()
