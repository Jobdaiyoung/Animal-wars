import json


class DB:
    def __init__(self):
        with open('PlayerDB.json', 'r') as player_file:
            self.player_dict = json.load(player_file)

    def create_db(self, player_name):
        """this function will create the data to PlayerDB.json"""
        while True:
            if player_name in self.player_dict:
                print('Sorry, the name was taken')
                print("please try again")
                player_name = input('What is your name?: ')
            else:
                new_data = {
                    player_name: {
                        "win": 0,
                        "lose": 0,
                        "win rate": 0
                    }
                }
                self.player_dict.update(new_data)
                with open('PlayerDB.json', "w") as player_file:
                    json.dump(self.player_dict, player_file, indent=4)
                print(f'Welcome {player_name}!')
                print('================================')
                return player_name

    def load_db(self, player_name):
        """this function will check that the name is in the database or not"""
        if player_name in self.player_dict:
            print(f'Welcome back {player_name}!')
            print('================================')
            return True
        else:
            print("This name hasn't register yet")
            print('================================')
            print("This name will [auto registered]")
            print('================================')
            return False

    def update_db(self, player):
        """update data to database"""
        self.player_dict[player.name] = player.stats
        with open('PlayerDB.json', "w") as player_file:
            json.dump(self.player_dict, player_file, indent=4)

    def show_db(self, player_name):
        """show the data of the player"""
        print(f'{player_name} stats')
        print(f'win: {self.player_dict[player_name]["win"]}', end=' ')
        print(f'lose: {self.player_dict[player_name]["lose"]}', end=' ')
        print(f'win rate: {self.player_dict[player_name]["win rate"]:.2f} %')
        print('================================')





