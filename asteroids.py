import numpy as np
import pygame
import time
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

    #Player parameters
    def __init__(self):
        pass

    #Moves the player forward
    def thrust(self):
        pass
    
    #Rotates the player
    def rotating(self):
        pass

    #Lets the player shoot bullets
    def shoot(self):
        pass

    #Creates the player
    def draw(self, win):
        pass
        
#endregion

#region Bullet

class Bullet():
    
    #Bullet parameters
    def __init__(self):
        pass

    #Moves the bullet
    def move(self):
        pass 

    #Creates the bullets
    def draw(self, win):
        pass

#endregion
 
#region Enemy

class Enemy():

    #Asteroid parameters
    def __init__(self):
        pass
    
    #Sets the different asteroid types
    def asteroid_type(self):
        pass

    #Breaks the asteroids to smaller parts
    def asteroid_break(self):
        pass

    #Moves the asteroids
    def move(self):
        pass           

    #Creates the Asteroids
    def draw(self, win):
        pass

#endregion

#region Main Functions

#Draws everything to the window
def draw_window(win, score):

    #Draws the score
    text = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    #Updates the display
    pygame.display.update()

#This is the main function for the game
def main():
    #Sets variables
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0
    run = True
    
    #Main game loop
    while run:
        pygame.time.delay(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break
        
        #Adds to the score
        score += 1

        #Creates the window
        win.fill(BACKGROUND)
        draw_window(win, score)

#Calls main
main()

#endregion