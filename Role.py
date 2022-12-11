class Dog:
    def __init__(self, max_hp=120, atk=15, speed=10):
        self.max_hp = max_hp
        self.hp = max_hp
        self.atk = atk
        self.speed = speed
        self.skills = {"skill": {"name": 'Double attack', "cost": 20},
                       "ult": {"name": 'Bite', "cost": 50}}

    @property
    def max_hp(self):
        return self.__max_hp

    @max_hp.setter
    def max_hp(self, new_max_hp):
        self.__max_hp = new_max_hp

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, new_hp):
        self.__hp = new_hp

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, new_atk):
        self.__atk = new_atk

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, new_speed):
        self.__speed = new_speed

    def __str__(self):
        return 'Dog'


class Cat:
    def __init__(self, max_hp=100, atk=20, speed=15):
        self.max_hp = max_hp
        self.hp = max_hp
        self.atk = atk
        self.speed = speed
        self.skills = {"skill": {"name": 'Slash claw', "cost": 30},
                       "ult": {"name": 'Pleading eyes', "cost": 60}}

    @property
    def max_hp(self):
        return self.__max_hp

    @max_hp.setter
    def max_hp(self, new_max_hp):
        self.__max_hp = new_max_hp

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, new_hp):
        self.__hp = new_hp

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, new_atk):
        self.__atk = new_atk

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, new_speed):
        self.__speed = new_speed

    def __str__(self):
        return 'Cat'


class Turtle:
    def __init__(self, max_hp=180, atk=15, speed=3):
        self.max_hp = max_hp
        self.hp = max_hp
        self.atk = atk
        self.speed = speed
        self.skills = {"skill": {"name": 'Strike', "cost": 30},
                       "ult": {"name": 'Heal', "cost": 70}}

    @property
    def max_hp(self):
        return self.__max_hp

    @max_hp.setter
    def max_hp(self, new_max_hp):
        self.__max_hp = new_max_hp

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, new_atk):
        self.__atk = new_atk

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, new_speed):
        self.__speed = new_speed

    def __str__(self):
        return 'Turtle'
