import random
from DB import *
from Player import Player
from Role import *


def setup_name():
    while True:
        print(f'{"(1) New Player         (2) Load Player"}')
        choice = input('Enter number: ')
        if choice == '1':
            name = input('What is your name?: ')
            return DB().create_db(name)
        elif choice == '2':
            name = input('What is your name?: ')
            if DB().load_db(name):
                return name
            else:
                DB().create_db(name)
                return name
        else:
            print('Invalid choice')
            print('================================')


def random_role():
    role_list = [Dog(), Cat(), Turtle()]
    p1_role = random.choice(role_list)
    role_list.remove(p1_role)
    p2_role = random.choice(role_list)
    return p1_role, p2_role


def setup_player():
    p1_role, p2_role = random_role()
    print('Welcome Player1')
    p1 = Player(setup_name(), p1_role)
    print('Welcome Player2')
    p2 = Player(setup_name(), p2_role)
    DB().show_db(p1.name)
    DB().show_db(p2.name)
    return p1, p2
