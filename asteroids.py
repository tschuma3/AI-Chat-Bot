import numpy as np
import pygame
import time

#region Player

class Player():

    VELOCITY = 5
    HEALTH = 1

    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.velocity = self.VELOCITY 
        self.health = self.HEALTH

    def keyboard(self):
        if key == pygame.k_w:
            self.y = self.y + self.velocity
        elif key == pygame.k_s:
            self.y = self.y + self.velocity
        elif key == pygame.K_a:
            self.x = self.x + self.velocity
        elif key == pygame.K_d:
            self.x = self.x + self.velocity

#endregion

#region Enemy

class Enemy():

    HEALTH = 1

    def __init__(self, velocity, health, targeting):
        self.velocity = velocity
        self.health = self.HEALTH
        self.targeting = targeting

    def targeting(self, targeting_time):
        pass
    
    def asteroid_type(self, aster_type):
        if aster_type == 1:
            self.velocity = 1
            self.health = self.health
            self.targeting = time.time() * 2
        elif aster_type == 2:
            self.velocity = 2
            self.health = self.health
            self.targeting = time.time() * 1.5
        elif aster_type == 3:
            self.velocity = 3
            self.health = self.health
            self.targeting = time.time() * 1

#endregion