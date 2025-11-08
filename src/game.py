"""
Contains various classes for the game

Status: Not finished
"""
class Game:
    #Todo
    pass

class Character:

    def __init__(self, name, health, alive=True):
        self.name = name
        self.health = health
        self.alive = alive
    
    def __repr__(self):
        return f"{self.name}\nHealth = {self.health}"

    def isAlive(self):
        if(self.health < 0):
            self.alive = False  

    def take_damage(self, amount):
        self.health -= amount

    