import random
from DB import DB


def random_damage(atk):
    """random the damage"""
    damage_multiply = [0, 0.6, 1, 1.2]
    popularity = [2, 42, 50, 6]
    multiply = random.choices(damage_multiply, popularity)
    if multiply[0] == 0:
        print('MISS!!')
    elif multiply[0] == 0.6:
        print('Hit!')
    elif multiply[0] == 1:
        print('Big Hit!')
    elif multiply[0] == 1.2:
        print('Critical Hit!!!')
    return atk * multiply[0]


def update_hp(p, damage):
    """update the player's hp"""
    if p.status['hp'] > damage:
        p.status['hp'] -= damage
    else:
        p.status['hp'] = 0


def next_round(p1_hp, p2_hp):
    return p1_hp > 0 and p2_hp > 0


def show_info(p1, p2):
    """show the status of each player"""
    print('*' * 64)
    print(f'{p1.name}: {p1.role}')
    print(f'{p2.name}: {p2.role}')
    print('+------------------------------++------------------------------+')
    print(f'|{p1.name:^30}||{p2.name:^30}|')
    print('+------------------------------++------------------------------+')
    print(f'|{"Status":^30}||{"Status":^30}|')
    print(f'| {"HP":<14}', end='')
    print(f'{int(p1.status["hp"]):>10}/{p1.status["max hp"]} |', end='')
    print(f'| {"HP":<14}', end='')
    print(f'{int(p2.status["hp"]):>10}/{p2.status["max hp"]} |')
    print(f'| {"ATK":<14}', end='')
    print(f'{p1.status["atk"]:>14} |', end='')
    print(f'| {"ATK":<14}', end='')
    print(f'{p2.status["atk"]:>14} |')
    print(f'| {"Energy":<14}', end='')
    print(f'{p1.status["energy"]:>14} |', end='')
    print(f'| {"Energy":<14}', end='')
    print(f'{p2.status["energy"]:>14} |')
    print('+------------------------------++------------------------------+')
    print(f'|{"Skills":^30}||{"Skills":^30}|')
    print(f'| {p1.skills["skill"]["name"]:<14}', end='')
    print(f'{p1.skills["skill"]["cost"]:>14} |', end='')
    print(f'| {p2.skills["skill"]["name"]:<14}', end='')
    print(f'{p2.skills["skill"]["cost"]:>14} |')
    print(f'| {p1.skills["ult"]["name"]:<14}', end='')
    print(f'{p1.skills["ult"]["cost"]:>14} |', end='')
    print(f'| {p2.skills["ult"]["name"]:<14}', end='')
    print(f'{p2.skills["ult"]["cost"]:>14} |')
    print('+------------------------------++------------------------------+')
    print('*' * 64)


def play(p1, p2):
    """actions phase of the player"""
    print(f"{p1.name}'s turn")
    while True:
        print(f'{"Please select actions":^64}')
        print(f'{"(1) Attack         (2) Use skills":^64}')
        choice = input('Enter number: ')
        print('='*64)
        if choice == '1':
            p1.attack(p2)
            print('=' * 64)
            break
        elif choice == '2':
            if p1.status['energy'] >= p1.skills["skill"]['cost']:
                while True:
                    print('List of skills')
                    print(f'1) {p1.skills["skill"]["name"]}')
                    print(f'2) {p1.skills["ult"]["name"]}')
                    print('=' * 64)
                    skill = int(input('Please select skill: '))
                    if skill == 1:
                        p1.special_move(p2, p1.skills["skill"])
                        print('=' * 64)
                        break
                    elif skill == 2:
                        if p1.status['energy'] >= p1.skills["ult"]['cost']:
                            p1.special_move(p2, p1.skills["ult"])
                            print('=' * 64)
                            break
                        else:
                            print(f'No enough energy for '
                                  f'{p1.skills["ult"]["name"]}')
                    else:
                        print('Invalid choice')
                        print('=' * 64)
                break
            else:
                print('No enough energy for any skills')
                print('=' * 64)
        else:
            print('Invalid choice')
            print('=' * 64)


def cal_win_rate(player):
    """calculate the win rate"""
    if player.stats['win'] == 0:
        return 0
    else:
        return (player.stats['win'] /
                (player.stats['win'] + player.stats['lose']))*100


def decide_winner(p1, p2):
    """decide who is the winner"""
    if p1.status['hp'] <= 0:
        p1.stats['lose'] += 1
        p2.stats['win'] += 1
        print(f'{p1.name} runs out of hp')
        print(f'{p2.name} is the winner!')
    elif p2.status['hp'] <= 0:
        p1.stats['win'] += 1
        p2.stats['lose'] += 1
        print(f'{p2.name} runs out of hp')
        print(f'{p1.name} is the winner!')
    p1.stats['win rate'] = cal_win_rate(p1)
    p2.stats['win rate'] = cal_win_rate(p2)
    DB().update_db(p1)
    DB().update_db(p2)
    print('Players stat auto updated')


def battle(p1, p2):
    """show info, decide who will play first, and let the players fight"""
    while True:
        show_info(p1, p2)
        if next_round(p1.status['hp'], p2.status['hp']):
            if p1.status['speed'] > p2.status['speed']:
                play(p1, p2)
                show_info(p1, p2)
                if next_round(p1.status['hp'], p2.status['hp']):
                    play(p2, p1)
                else:
                    break
            else:
                play(p2, p1)
                show_info(p1, p2)
                if next_round(p1.status['hp'], p2.status['hp']):
                    play(p1, p2)
                else:
                    break
        else:
            break
