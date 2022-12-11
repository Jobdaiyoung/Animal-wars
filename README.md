# ANIMAL WARS

## Overview
Animal wars is a pvp turn-based game that the game will randomly give the player a different role with different skills to fight each other.Who runs out of hp first will lose. 


## Features
- turn-based 2 player pvp game that each player will fight each others.
- the player can use skills to fight each others.
- player stats save/load management.

## Requirement
- Python version 3.10 or later
- PlayerDB.json file
- random Module

## Gameplay
- the program will ask players to load save or create new save that contains player's wins, loses, and win rate.
- the program will randomly give the different role to each player which have unique skills.
- each player have to select their action, attack or use skill, in their turns.
- the player who runs out of hp first will lose the game.
- the program will update the wins, loses, and win rate of the player automatically. Detail of all classes

## Details of all classes
- #### Dog, Cat, Turtle in Role.py
these classes are the roles in the game and contain the status of the player which are hp, max hp, atk, speed, skills.
- #### DB in DB.py
this class will create and update the player stats to the PlayerDB.json file and also load stats from it too.
- #### Player in Player.py
this class contains detail of the player such as name, and stats and also generate the action of the player.

## Code structure
- #### main.py
main file that will run the program by using every function and class to work together.
- #### Player.py
contains class Player
- #### DB.py
contains class DB
- #### Role.py
contains class Dog,Cat,Turtle
- #### Setup.py
contains functions that is used to create a Player
- #### game_function.py
contains functions that is used in battle phase of the game
- #### PlayerDB.json
contains all of player's stats which are wins, loses, and win rate