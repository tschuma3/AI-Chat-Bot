import numpy as np
import random
import pygame
import time
import os
pygame.font.init()
pygame.init()

#Window width and height
WIN_WIDTH = 1400
WIN_HEIGHT = 1000
BACKGROUND = (0, 0, 0)

#Create fonts for the score
STAT_FONT = pygame.font.SysFont("comicsans", 25)

PLAYER_IMG = pygame.transform.scale_by(pygame.image.load(os.path.join("Images", "Kirby.png")), (0.02, 0.02))
BULLET_IMG = pygame.transform.scale_by(pygame.image.load(os.path.join("Images", "Smash Ball.png")), (0.02, 0.02))
ASTEROID_MAGENTA = pygame.transform.scale_by(pygame.image.load(os.path.join("Images", "Magenta Asteroid.png")), (0.5, 0.5))
ASTEROID_GREEN = pygame.transform.scale_by(pygame.image.load(os.path.join("Images", "Green Asteroid.png")), (0.5, 0.5))
ASTEROID_WHITE = pygame.transform.scale_by(pygame.image.load(os.path.join("Images", "White Asteroid.png")), (0.5, 0.5))

BULLETS = []
ENEMIES = []

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
        self.dimension = self.img.get_size()

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
        self.position = screen_wrapper(self.position, self.dimension)
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
        self.dimension = self.img.get_size()

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
        self.position = screen_wrapper(self.position, self.dimension)
        blitRotateCenter(win, self.img, self.position, self.angle)

#endregion
 
#region Enemy

class Enemy():
    IMG_MAGENTA = ASTEROID_MAGENTA
    IMG_GREEN = ASTEROID_GREEN
    IMG_WHITE = ASTEROID_WHITE

    #Asteroid parameters
    def __init__(self, x, y, angle, aster_type):
        self.angle = angle
        self.velocity = 8
        self.x = x
        self.y = y
        self.position = pygame.math.Vector2(self.x, self.y)
        self.aster_type = aster_type

        self.img_magenta = self.IMG_MAGENTA
        self.img_green = self.IMG_GREEN
        self.img_white = self.IMG_WHITE

        self.rect_magenta = self.img_magenta.get_rect()
        self.rect_green = self.img_green.get_rect()
        self.rect_white = self.img_white.get_rect()

        self.dimension_magenta = self.img_magenta.get_size()
        self.dimension_green = self.img_green.get_size()
        self.dimension_white = self.img_white.get_size()
    
    #Sets the different asteroid types
    def asteroid_type(self):
        if self.aster_type == 1:
            self.velocity = 2
        elif self.aster_type == 2:
            self.velocity = 5
        elif self.aster_type == 3:
            self.velocity == 8

    #Breaks the asteroids to smaller parts
    def asteroid_targeting(self):
        pass

    #Moves the asteroids
    def move(self):
        velocity_x = 0
        velocity_y = 0
        velocity_x += self.velocity * np.cos(np.radians(self.angle + 90)) 
        velocity_y -= self.velocity * np.sin(np.radians(self.angle + 90))

        self.tick_count = 0
        self.position += (velocity_x, velocity_y)
        #self.rect.center = self.position          

    #Creates the Asteroids
    def draw(self, win):
        if self.aster_type == 1:
            self.position = screen_wrapper(self.position, self.dimension_magenta)
            blitRotateCenter(win, self.img_magenta, self.position, self.angle)
        elif self.aster_type == 2:
            self.position = screen_wrapper(self.position, self.dimension_green)
            blitRotateCenter(win, self.img_green, self.position, self.angle)
        elif self.aster_type == 3:
            self.position = screen_wrapper(self.position, self.dimension_white)
            blitRotateCenter(win, self.img_white, self.position, self.angle)

class Magenta_Asteroid(Enemy):

    def __init__(self, x, y, angle):
        super(Enemy, self).__init__()
        
class Green_Asteroid(Enemy):

    def __init__(self, x, y, angle):
        super(Enemy, self).__init__()

class White_Asteroid(Enemy):

    def __init__(self, x, y, angle):
        super(Enemy, self).__init__()   

#endregion

#region Main Functions

def screen_wrapper(position, dimension):
    if position.x < -dimension[0]:
        position.x = WIN_WIDTH + (dimension[0] // 4)
    elif position.x > WIN_WIDTH + (dimension[0] // 4):
        position.x = -dimension[0]
    if position.y < -dimension[1]:
        position.y = WIN_HEIGHT + (dimension[1] // 4)
    elif position.y > WIN_HEIGHT + (dimension[1] // 4):
        position.y = -dimension[1]
    return position    

#Rotate a surface and blit it to the window
def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    surf.blit(rotated_image, new_rect.topleft)

#Draws everything to the window
def draw_window(win, timer, score, player, bullet, enemy):

    player.draw(win)

    for bullet in BULLETS:
        if timer >= 100:
            BULLETS.remove(bullet)
        bullet.draw(win)
    print(len(BULLETS))

    for enemy in ENEMIES:
        enemy.draw(win)

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

    for i in range(15):
            enemy = Enemy(random.randrange(0, WIN_WIDTH), random.randrange(0, WIN_HEIGHT), random.randrange(0, 360), random.randrange(1, 4))
            ENEMIES.append(enemy)
    
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
        
        for enemy in ENEMIES:
            enemy.asteroid_type()
            enemy.move()

        #Creates the window
        win.fill(BACKGROUND)
        draw_window(win, timer, score, player, bullet, enemy)

#Calls main
main()

#endregion