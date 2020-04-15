import pygame
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
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 4
enemyY_change = 40

def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x,y):
    screen.blit(enemyImg, (x, y))

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
        
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()