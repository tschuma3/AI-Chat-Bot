import numpy as np
import pygame
import time
import os
import random
import pickle
import neat
pygame.font.init()
pygame.display.init()
pygame.init()

#Window width and height
WIN_WIDTH = 800
WIN_HEIGHT = 800
BACKGROUND = (255, 255, 255)

BULLET_ARRAY = []
ENEMY_ARRAY = []

#Generations
Gen = 0

#Create fonts for the score
STAT_FONT = pygame.font.SysFont("comicsans", 50)

#region Player

class Player():

    VELOCITY = 15
    HEALTH = 1

    def __init__(self, x, y, dim_x, dim_y, health):
        self.x = x
        self.y = y
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.velocity = self.VELOCITY 
        self.health = self.HEALTH

    def keyboard(self):
        global BULLET_ARRAY
        bullet = Bullet()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.y > 0:
            self.y = self.y - self.velocity
        elif keys[pygame.K_s] and self.y < WIN_HEIGHT - self.dim_y:
            self.y = self.y + self.velocity
        elif keys[pygame.K_a] and self.x > 0:
            self.x = self.x - self.velocity
        elif keys[pygame.K_d] and self.x < WIN_WIDTH - self.dim_x:
            self.x = self.x + self.velocity
        elif keys[pygame.K_SPACE]:
            BULLET_ARRAY.append(bullet)

    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.dim_x, self.dim_y))
        
#endregion

#region Bullet

class Bullet():
    
    def __init__(self, x, y):
        self.velocity = 10
        self.damage = 1
        self.dim_x = 10
        self.dim_y = 10
        self.x = 0
        self.y = 0

    def move(self):
        self.velocity 

    def draw(self, win, player_x, player_y):
        pygame.draw.rect(win, (0, 255, 0), (player_x, player_y, self.dim_x, self.dim_y))

#endregion
 
#region Enemy

class Enemy():

    HEALTH = 1

    def __init__(self, velocity, aster_type, targeting, health):
        self.velocity = velocity
        self.x = random.randrange(0, WIN_WIDTH)
        self.y = random.randrange(0, WIN_HEIGHT)
        self.health = self.HEALTH
        self.targeter = targeting
        self.aster_type = aster_type
    
    def asteroid_type(self, aster_type):
        if self.aster_type == 1:
            self.velocity = 1
            self.health = self.health
            self.targeter = self.velocity * time.time * 1
        elif self.aster_type == 2:
            self.velocity = 2
            self.health = self.health
            self.targeting = self.velocity * time.time * 2
        elif self.aster_type == 3:
            self.velocity = 3
            self.health = self.health
            self.targeting = self.velocity * time.time * 3             

    def draw(self, win):
        pygame.draw.circle(win, (255, 0, 255), (self.x, self.y), 20)

#endregion

#region Main Functions

def draw_window(win, player, bullet, enemies, score):
    #win.blit(BACKGROUND, (0, 0))

    player.draw(win)

    for bullet in BULLET_ARRAY:
        bullet.move()
        bullet.draw(win, player.x, player.y)
    
    """
    for enemy in enemies:
        enemy.draw(win)
    """

    #Draws the score
    text = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    pygame.display.update()

def main():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0
    run = True
    player = Player(100, 200, 20, 20, 1)
    bullet = Bullet()
    enemies = []
    rand = random.randrange(0, 3)
    
    """
    for i in range(15):
        enemy = Enemy(15, rand, (player.x, player.y), 1)
        enemies.append([enemy, enemy.asteroid_type(rand)])
    """
    
    while run:
        pygame.time.delay(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break

        player.keyboard()
        
        win.fill((0, 0, 0))

        score += 1
        
        draw_window(win, player, bullet, enemies, score)

main()

#endregion