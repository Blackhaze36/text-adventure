#! /usr/bin/env python3
# Main game logic. Run this files to launch game
# Created by Brandon Thomas
import time
from character import Character

# welcome splash
print ("|~~~~~~~~~~~~~~~~~~~~~~~~|")
print ("|~Welcome to the Dungeon~|")
print ("|~~~~~~~~~~~~~~~~~~~~~~~~|")

time.sleep(0)

# Initializes the player character.
player = Character("Brandon", 100, 100, {})

