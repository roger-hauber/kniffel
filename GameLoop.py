### Game Loop Skeleton
#import Class stuff from other script
from PlayerClass import KniffelPlayer
import PlayerClass
import random

# while loop with i < 13 -> after 13 rounds the game is finished
# but for now choose lower threshold
i = 0

#Game starts with Input from Users providing all player names
player_names = input("Willkommen bei Kniffel!\nBitte gebt eure Namen ein getrennt durch Leerzeichen..\n\n\n")

player_names = player_names.split()

#Create list of KniffelPlayer instances with the given names
players = [KniffelPlayer(name) for name in player_names]

#now start the game loop
while i < 4:
    for player in players:
        player.still_open()
        player.one_turn()
    i += 1
