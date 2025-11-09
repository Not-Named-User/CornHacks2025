"""
Contains various classes for the game

Status: Not finished
"""
import pygame
class Game:
    #Todo
    def __init__(self, level):
        pass


class Level(Game):
    pass

class Player(pygame.sprite.Sprite):    # Child class of Parent class character
    
    def __init__(self, health, position, raidus=25, color=(0, 255, 0)):
        super.__init__()
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.position = list(position)

<<<<<<< HEAD
    def isAlive(self):
        if(self.health < 0):
            self.alive = False  

    def take_damage(self, amount):
        self.health -= amount

    """
Player Class for Super Loud

Status: Not finished
"""
import game
class Player(game.Character):    # Child class of Parent class character

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
    
=======
>>>>>>> PreLaunch
    def printCharacterStats(self):
        print(f"Name: {self.name}, Health: {self.health} Level: {self.level}")

class Enemy(Character):
    pass
    