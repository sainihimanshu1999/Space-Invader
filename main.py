import pygame
import math
import random

#initilaizing pygame
pygame.init()

#creating the screen
screen = pygame.display.set_mode((800, 600))

#Background
background = pygame.image.load('background.png')

#Changing title and the icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('player.png') 
playerX = 370
playerY = 480
playerX_change = 0

#enemy
enemyImg = pygame.image.load('alien.png') 
enemyX = random.randint(0,735)
enemyY = random.randint(50,150)
enemyX_change = 4 
enemyY_change = 40

#Bullet
#Ready -  no bullet shown
#Fire - moving bullet
bulletImg = pygame.image.load('bullet.png') 
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

score = 0


def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x,y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


#game loop
running = True
while running:
    #adding background in the screen RGB
    screen.fill((0, 0, 255))
    #adding background image
    screen.blit(background , (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Checking the keystroke that wheter it is left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = +5
            #firing pf bullet using space fucntion
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerX_change = 0
            if event.key == pygame.K_RIGHT:
                playerX_change = 0
    #defining boundary for player
    playerX += playerX_change
    if playerX <=0:
        playerX = 0
    elif playerX >=736:
        playerX = 736
    #defining boundary for the enemy
    enemyX += enemyX_change
    if enemyX <=0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >=736:
        enemyX_change = -4
        enemyY += enemyY_change

    #Bullet Movement
    if bulletY <= 0 :
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    #collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision: 
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0,735)
        enemyY = random.randint(50,150)
        
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()