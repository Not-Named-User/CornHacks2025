"""
Player Class for Super Loud

Status: Not finished
"""
import game
class Player(Character):    # Child class of Parent class character

    def __init__(self, name, health = 10, level = 1):
        self.name = name
        self.health = health
        self.level = level

    def __repr__(self):
        return f"{self.name}\nHealth = {self.health}, Level = {self.level}"
        #print(f"{self.name}: Health = {self.health}, Level = {self.level}")
    
    def heal(self, amount):
        self.health += amount
        if self.health > 10:
            self.health = 10

    def level_up(self):
        self.level += 1
    
    def printCharacterStats(self):
        print(f"Name: {self.name}, Health: {self.health} Level: {self.level}")
    