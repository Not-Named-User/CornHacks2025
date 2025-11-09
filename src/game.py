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


    def printCharacterStats(self):
        print(f"Name: {self.name}, Health: {self.health} Level: {self.level}")

class Enemy(Character):
    pass
    