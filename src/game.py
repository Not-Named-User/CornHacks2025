"""
Contains various classes for the game

Status: Not finished
"""
import pygame
import math
class Game:
    #Todo
    def __init__(self, level):
        pass



class Level(Game):
    pass

class Player(pygame.sprite.Sprite):    # Child class of Parent class character
    
    def __init__(self, pos, health = 3, radius=25, color=(0, 255, 0)):
        super().__init__()
        self.image = pygame.image.load("../assets/images/gorilla.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = (self.pos)
        self.health = health
        self.timeBoost = 0
        self.projectile_speed = 10
        self.bullet_size = 10

    def isAlive(self):
        if self.health <= 0:
            return False
        else:
            return True
    
    def shoot(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        #print(f"Mouse pos: ({mouse_x}, {mouse_y})")
        bullet = Projectile(self.pos.x-80, self.pos.y - 40, mouse_x, mouse_y, self.projectile_speed, (100, 100, 100), self.bullet_size)

        return bullet

    def move(self, keys):
        if keys[pygame.K_w]:
            self.pos.y -= 10
            self.rect.centery = self.pos.y
        if keys[pygame.K_s]:
            self.pos.y += 10
            self.rect.centery = self.pos.y
        if keys[pygame.K_a]:
            self.pos.x -= 10
            self.rect.centerx = self.pos.x
        if keys[pygame.K_d]:
            self.pos.x += 10
            self.rect.centerx = self.pos.x
        if keys[pygame.K_LSHIFT]:
            self.timeBoost = 100
        
class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, pos, health=1, radius=25, color=(32, 85, 208)):
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        #self.screen = screen
        self.image.fill("blue")
        self.rect = self.image.get_rect()
        self.rect.center = (300, 400)
        self.pos = pos
        self.health = health

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, target_x, target_y, speed, color, radius):
        super().__init__()

        self.image = pygame.image.load("../assets/images/banana.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()

        self.rect = self.image.get_rect(center=(x, y))

        # Calculate direction vector
        dx = target_x - x
        dy = target_y - y
        distance = math.sqrt(dx**2 + dy**2)
        if distance == 0:  # Avoid division by zero
            self.vel_x = 0
            self.vel_y = 0
        else:
            self.vel_x = (dx / distance) * speed
            self.vel_y = (dy / distance) * speed

    def checkState(self, object):
        if(pygame.sprite.groupcollide(self, object, True)  == True ):
            return 1

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
