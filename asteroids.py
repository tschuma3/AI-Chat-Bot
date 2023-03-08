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
        self.acceleration = 2
        self.max_speed = 25
        self.velocity = pygame.math.Vector2(0, 0)
        self.position = pygame.math.Vector2(x, y)

        self.img = self.IMG
        self.rect = self.img.get_rect()
        self.dimension = self.img.get_size()

    #Moves the player forward
    def thrust(self):
        print('Up')
        acceleration_x = -self.acceleration * np.sin(np.radians(self.angle)) 
        acceleration_y = -self.acceleration * np.cos(np.radians(self.angle))
        self.velocity.x += acceleration_x
        self.velocity.y += acceleration_y
        speed = self.velocity.magnitude()
        if speed > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)
        self.position += self.velocity
        self.rect.center = self.position

    #Rotates the player
    def rotate(self, direction):
        self.angle += direction 
        self.angle %= 360
        print('Rotate')

    #Lets the player shoot bullets
    def shoot(self):
        global BULLETS
        bullet = Bullet(self.rect.centerx, self.rect.centery, self.angle)
        BULLETS.append(bullet)
        print('Space')

    def actions(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.thrust()
        if keys[pygame.K_LEFT]:
            self.rotate(10)
        if keys[pygame.K_RIGHT]:
            self.rotate(-10)
        if keys[pygame.K_SPACE]:
            shooting = True
            if shooting:
                shooting = False
                self.shoot()
        
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
        self.velocity = pygame.math.Vector2(5, 5)
        self.position = pygame.math.Vector2(x, y)

        self.img = self.IMG
        self.mask = pygame.mask.from_surface(self.img)
        self.rect = self.img.get_rect()
        self.dimension = self.img.get_size()

    #Moves the bullet
    def move(self):
        velocity_x = self.velocity.x * np.cos(np.radians(self.angle)) 
        velocity_y = self.velocity.y * np.sin(np.radians(self.angle))
        self.velocity += (velocity_x, velocity_y)
        self.position += self.velocity
        self.rect.center += self.position 

    #Creates the bullets
    def draw(self, win):
        self.position = screen_wrapper(self.position, self.dimension)
        blitRotateCenter(win, self.img, self.position, self.angle)

#endregion
 
#region Enemy

class Enemy():

    #Asteroid parameters
    def __init__(self, x, y, angle, aster_type):
        self.angle = angle
        self.velocity = pygame.math.Vector2(0, 0)
        self.max_speed = 0
        self.acceleration = 0.1
        self.position = pygame.math.Vector2(x, y)
        self.aster_type = aster_type

    #Breaks the asteroids to smaller parts
    def asteroid_targeting(self, player_position, player_velocity):

        """
        Use: https://www.youtube.com/watch?v=OxHJ-o_bbzs
        5.4 Arrive Steering Behavior - The Nature of Code by The Coding Train for the physics 
        """
        #if self.aster_type == 1:
        desired_velocity = (self.position - player_position).normalize() * self.max_speed
        steering = self.velocity - pygame.math.Vector2(desired_velocity)
        self.velocity += steering 
        self.position += self.velocity

    #Moves the asteroids
    def move(self):
        # velocity_x = self.velocity.x * np.cos(np.radians(self.angle + 90)) 
        # velocity_y = self.velocity.y * np.sin(np.radians(self.angle + 90))
        # self.position += (velocity_x, velocity_y)

        acceleration_x = -self.acceleration * np.sin(np.radians(self.angle)) 
        acceleration_y = -self.acceleration * np.cos(np.radians(self.angle))
        self.velocity.x += acceleration_x
        self.velocity.y += acceleration_y
        speed = self.velocity.magnitude()
        if speed > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)
        self.position += self.velocity         

    #Creates the Asteroids
    def draw(self, win):
        raise NotImplementedError

class Magenta_Asteroid(Enemy):
    IMG_MAGENTA = ASTEROID_MAGENTA

    def __init__(self, x, y, angle):
        super().__init__(x, y, angle, 1)
        self.img = self.IMG_MAGENTA
        self.rect = self.img.get_rect()
        self.dimension = self.img.get_size()
        self.mask = pygame.mask.from_surface(self.img)
        self.velocity = pygame.math.Vector2(2, 2)
        self.max_speed = 2

    def draw(self, win):
        self.position = screen_wrapper(self.position, self.dimension)
        blitRotateCenter(win, self.img, self.position, self.angle)
        
class Green_Asteroid(Enemy):
    IMG_GREEN = ASTEROID_GREEN

    def __init__(self, x, y, angle):
        super().__init__(x, y, angle, 2)
        self.img = self.IMG_GREEN
        self.rect = self.img.get_rect()
        self.dimension = self.img.get_size()
        self.mask = pygame.mask.from_surface(self.img)
        self.velocity = pygame.math.Vector2(4, 4)
        self.max_speed = 4

    def draw(self, win):
        self.position = screen_wrapper(self.position, self.dimension)
        blitRotateCenter(win, self.img, self.position, self.angle)

class White_Asteroid(Enemy):
    IMG_WHITE = ASTEROID_WHITE

    def __init__(self, x, y, angle):
        super().__init__(x, y, angle, 3) 
        self.img = self.IMG_WHITE
        self.rect = self.img.get_rect()
        self.dimension = self.img.get_size()
        self.mask = pygame.mask.from_surface(self.img)
        self.velocity = pygame.math.Vector2(6, 6)
        self.max_speed = 6

    def draw(self, win):
        self.position = screen_wrapper(self.position, self.dimension)
        blitRotateCenter(win, self.img, self.position, self.angle)

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
def draw_window(win, score, player, bullet, enemy):

    player.draw(win)

    for bullet in BULLETS:
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
    bullet = Bullet(player.position.x, player.position.y, player.angle)
    score = 0
    run = True

    for i in range(15):
        x = random.randrange(0, WIN_WIDTH)
        y = random.randrange(0, WIN_HEIGHT)
        angle = random.randrange(0, 360)
        aster_type = random.randrange(1, 4)
        if aster_type == 1:
            enemy = Magenta_Asteroid(x, y, angle)
        elif aster_type == 2:
            enemy = Green_Asteroid(x, y, angle)
        else:
            enemy = White_Asteroid(x, y, angle)
        ENEMIES.append(enemy)
    
    #Main game loop
    while run:
        pygame.time.delay(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break        

        #Adds to the score
        score += 1

        player.actions()

        for enemy in ENEMIES:
            enemy.asteroid_targeting(player.position, player.velocity)    
            enemy.move()

            # if pygame.sprite.collide_mask(enemy, player):
            #     print("Dead")
            #     ENEMIES.remove(enemy)

        for bullet in BULLETS:
            bullet.move()
            if bullet.position.y < 0 or bullet.position.y > WIN_HEIGHT or bullet.position.x < 0 or bullet.position.x > WIN_WIDTH:
                BULLETS.remove(bullet)

            for enemy in ENEMIES:
                if pygame.sprite.collide_mask(bullet, enemy):
                    BULLETS.remove(bullet)
                    ENEMIES.remove(enemy)

        #Creates the window
        win.fill(BACKGROUND)
        draw_window(win, score, player, bullet, enemy)

#Calls main
main()

#endregion