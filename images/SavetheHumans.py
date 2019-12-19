import math
import random
import time

import pygame
from pygame import mixer

pygame.init()

#Screen
screen = pygame.display.set_mode((1200, 700))

#Background image
background = pygame.image.load('space.png')

#The player
playerImg = pygame.image.load('destroyer1.png')
playerX = 370
playerY = 515
playerX_change = 0

#The enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 30

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('master.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

#The missile
bulletImg = pygame.image.load('missiletoe.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 50
bullet_state = "ready"

#Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 500
testY = 10

#Game over
over_font = pygame.font.Font('freesansbold.ttf', 54)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("THEY ATE EVERYONE AND IT'S YOUR FAULT", True, (255, 255, 255))
    screen.blit(over_text, (0, 300))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 65:
        return True
    else:
        return False


#Main loop
running = True
while running:

    screen.fill((0, 0, 0))
#Background
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#How to move
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -7
            if event.key == pygame.K_RIGHT:
                playerX_change = 7
            if event.key == pygame.K_SPACE:
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX +35
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1000:
        playerX = 1000

#Enemy movement
    for i in range(num_of_enemies):

#Game over
        if enemyY[i] > 500:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 25
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 1000:
            enemyX_change[i] = -25
            enemyY[i] += enemyY_change[i]
            

#When the enemy and bullet collide
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 600
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

#How the bullets move
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()
