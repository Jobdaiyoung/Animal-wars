from game_functions import random_damage, update_hp
import json


class Player:
    def __init__(self, name: str, role):
        self.name = name
        self.role = role
        self.status = {'hp': role.hp, 'atk': role.atk,
                       'speed': role.speed, 'max hp': role.max_hp,
                       'energy': 0}
        self.skills = role.skills
        with open('PlayerDB.json', 'r') as player_file:
            self.stats = json.load(player_file)[self.name]

    def attack(self, opponent):
        print(f'{self.name} attacks {opponent.name} with basic attack')
        damage = random_damage(self.status['atk'])
        update_hp(opponent, damage)
        print(f'{self.name} makes {int(damage)} damages')
        self.status['energy'] += 10

    def special_move(self, opponent, skill):
        print(f'{self.name} use {skill["name"]}!!!')
        if skill["name"] == 'Double attack':
            damage = random_damage(2*self.status['atk'])
            update_hp(opponent, damage)
            print(f'{self.name} makes {int(damage)} damages')
        elif skill["name"] == 'Bite':
            damage = 45
            update_hp(opponent, damage)
            print(f'{self.name} makes {int(damage)} damages')
        elif skill["name"] == 'Slash claw':
            damage = 1.2*self.status['atk']
            update_hp(opponent, damage)
            print(f'{self.name} makes {int(damage)} damages')
        elif skill["name"] == 'Pleading eyes':
            damage = random_damage(100)
            update_hp(opponent, damage)
            print(f'{self.name} makes {int(damage)} damages')
        elif skill["name"] == 'Strike':
            damage = self.status['atk']
            update_hp(opponent, damage)
            print(f'{self.name} makes {int(damage)} damages')
        elif skill["name"] == 'Heal':
            self.status['hp'] += 45
            print(f'{self.name} heal 45 hp')
        self.status['energy'] -= skill['cost']
