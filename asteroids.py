import numpy as np
import pygame
import time
import os
import random
import pickle
import neat
pygame.font.init()
pygame.init()

#Window width and height
WIN_WIDTH = 800
WIN_HEIGHT = 800
BACKGROUND = (0, 0, 0)

#Create fonts for the score
STAT_FONT = pygame.font.SysFont("comicsans", 25)

#region Player

class Player():

    def __init__(self):
        pass

    def thrust(self):
        pass

    def shoot(self):
        pass

    def draw(self, win):
        pass
        
#endregion

#region Bullet

class Bullet():
    
    def __init__(self):
        pass

    def move(self):
        pass 

    def draw(self, win):
        pass

#endregion
 
#region Enemy

class Enemy():

    def __init__(self):
        pass
    
    def asteroid_type(self):
        pass           

    def draw(self, win):
        pass

#endregion

#region Main Functions

def draw_window(win, score):

    #Draws the score
    text = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    pygame.display.update()

def main():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0
    run = True
    
    while run:
        pygame.time.delay(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break
        
        win.fill(BACKGROUND)

        score += 1
        
        draw_window(win, score)

main()

#endregion