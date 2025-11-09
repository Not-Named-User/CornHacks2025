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
    
    def __init__(self, pos, health = 3, radius=25, color=(0, 255, 0)):
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (300, 400)
        self.pos = pos
        self.health = health

    def isAlive(self):
        if self.health <= 0:
            return False
        else:
            return True

    def printCharacterStats(self):
        print(f"Name: {self.name}, Health: {self.health} Level: {self.level}")

class Enemy(pygame.sprite.Sprite):
    pass
    