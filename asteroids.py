import numpy as np
import pygame
import time
import os
pygame.font.init()
pygame.init()

#Window width and height
WIN_WIDTH = 800
WIN_HEIGHT = 800
BACKGROUND = (0, 0, 0)

#Create fonts for the score
STAT_FONT = pygame.font.SysFont("comicsans", 25)

PLAYER_IMG = pygame.transform.scale_by(pygame.image.load(os.path.join("Images", "Kirby.png")), (0.02, 0.02))
BULLET_IMG = pygame.transform.scale_by(pygame.image.load(os.path.join("Images", "Smash Ball.png")), (0.02, 0.02))

BULLETS = []

#region Player

class Player():
    IMG = PLAYER_IMG

    #Player parameters
    def __init__(self, x, y):
        self.angle = 0
        self.time = pygame.time.delay(10)
        self.velocity = (0, 0)
        self.x = x
        self.y = y
        self.position = pygame.math.Vector2(self.x, self.y)
        self.tick_count = 0

        self.img = self.IMG
        self.rect = self.img.get_rect()

    #Moves the player forward
    def thrust(self):
        print('Up')
        velocity_x = 0
        velocity_y = 0
        self.velocity = 8
        velocity_x += self.velocity * np.cos(np.radians(self.angle + 90)) 
        velocity_y -= self.velocity * np.sin(np.radians(self.angle + 90))

        self.tick_count = 0
        self.position += (velocity_x, velocity_y)
        self.rect.center = self.position

    #Rotates the player
    def rotate(self, direction):
        self.tick_count = 0
        self.angle += direction % 360
        print('Rotate')

    #Lets the player shoot bullets
    def shoot(self):
        global BULLETS
        bullet = Bullet(self.rect.centerx, self.rect.centery, self.angle)
        BULLETS.append(bullet)
        print('Space')

    def actions(self):
        self.tick_count += 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.thrust()
        if keys[pygame.K_LEFT]:
            self.rotate(20)
        if keys[pygame.K_RIGHT]:
            self.rotate(-20)
        if keys[pygame.K_SPACE]:
            shooting = True
            if shooting:
                shooting = False
                self.shoot()
    
    #Gives a mask for collision
    def mask(self):
        pass
        
    #Creates the player
    def draw(self, win):
        blitRotateCenter(win, self.img, self.position, self.angle)

#endregion

#region Bullet

class Bullet():
    IMG = BULLET_IMG

    #Bullet parameters
    def __init__(self, x, y, angle):
        self.angle = angle
        self.velocity = (0, 0)
        self.x = x
        self.y = y
        self.position = pygame.math.Vector2(self.x, self.y)

        self.img = self.IMG
        self.rect = self.img.get_rect()

    #Moves the bullet
    def move(self):
        velocity_x = 0
        velocity_y = 0
        self.velocity = 15
        velocity_x += self.velocity * np.cos(np.radians(self.angle + 90)) 
        velocity_y -= self.velocity * np.sin(np.radians(self.angle + 90))

        self.tick_count = 0
        self.position += (velocity_x, velocity_y)
        self.rect.center += self.position 

    #Creates the bullets
    def draw(self, win):
        blitRotateCenter(win, self.img, self.position, self.angle)

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

#Rotate a surface and blit it to the window
def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)

#Draws everything to the window
def draw_window(win, timer, score, player, bullet):

    player.draw(win)
    for bullet in BULLETS:
        if timer >= 100:
            BULLETS.remove(bullet)
        bullet.draw(win)
    
    print(len(BULLETS))

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
    player = Player(WIN_WIDTH / 2, WIN_HEIGHT / 2)
    bullet = Bullet(player.x, player.y, player.angle)
    score = 0
    run = True
    
    #Main game loop
    while run:
        pygame.time.delay(30)
        timer = clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break        

        #Adds to the score
        score += 1

        player.actions()

        for bullet in BULLETS:
            bullet.move()

        #Creates the window
        win.fill(BACKGROUND)
        draw_window(win, timer, score, player, bullet)

#Calls main
main()

#endregion