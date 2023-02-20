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
    VELOCITY = 5
    TORQUE = 5

    #Player parameters
    def __init__(self, x, y, win):
        self.rotation = np.pi / 6
        self.dimentions = (20, 20)
        self.health = 1
        self.player_pos = [x, y]
        self.player = pygame.draw.rect(win, (255, 0, 255), (self.player_pos, self.dimentions))

    #Moves the player forward
    def thrust(self):
        self.player_pos[1] += self.VELOCITY
        print('Forward')
    
    #Rotates the player
    def rotating(self, direction):
        if direction == "left":
            self.player_pos = pygame.transform.rotate(self.player, self.rotation)
            print('Turn Left')
        elif direction == "right":
            self.player_pos = pygame.transform.rotate(self.player, np.negative(self.rotation))
            print('Turn Right')

    #Lets the player shoot bullets
    def shoot(self):
        pass

    def mask(self):
        pass
        
    #Creates the player
    def draw(self, win):
        win.blit(win, self.player)

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
def draw_window(win, score, player):

    player.draw(win)

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
    player = Player(WIN_WIDTH / 2, WIN_HEIGHT / 2, win)
    run = True
    
    #Main game loop
    while run:
        pygame.time.delay(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break

        key = pygame.key.get_pressed()
        if key[pygame.K_UP]: 
            player.thrust()
        elif key[pygame.K_LEFT]:
            player.rotating("left")
        elif key[pygame.K_RIGHT]:
            player.rotating("right")        

        #Adds to the score
        score += 1

        #Creates the window
        win.fill(BACKGROUND)
        draw_window(win, score, player)

#Calls main
main()

#endregion