import pygame

#initilaizing pygame
pygame.init()

#creating the screen
screen = pygame.display.set_mode((800, 600))

#Changing title and the icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('player.png') 
playerX = 370
playerY = 480
playerX_change = 0

def player(x,y):
    screen.blit(playerImg, (x, y))

#game loop
running = True
while running:
    #adding background in the screen RGB
    screen.fill((0, 0, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Checking the keystroke that wheter it is left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.4
            if event.key == pygame.K_RIGHT:
                playerX_change = +0.4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerX_change = 0
            if event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <=0:
        playerX = 0
    elif playerX >=736:
        playerX = 736
    player(playerX, playerY)
    pygame.display.update()