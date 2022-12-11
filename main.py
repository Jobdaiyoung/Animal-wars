from game_functions import *
from Setup import *


def main():
    print('Animal Wars')
    p1, p2 = setup_player()
    battle(p1, p2)
    decide_winner(p1, p2)


if __name__ == '__main__':
    main()
