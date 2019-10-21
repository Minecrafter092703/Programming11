import pygame
import os
x = 0
y = 0
speed_x = 3
speed_y = 3
Lives = 0

#Importing image
_image_library = {}
def get_image(path):
        global _image_library
        image = pygame.image.load('ball.png')
               
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

#The screen where the pokeball bounces
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

#How the pokeball moves around the 
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True


##        pressed = pygame.key.get_pressed()
##        if pressed[pygame.K_UP]: y -= speed_y
##        if pressed[pygame.K_DOWN]: y += speed_y
##        if pressed[pygame.K_LEFT]: x -= speed_x
##        if pressed[pygame.K_RIGHT]: x += speed_x
        x = x+speed_x
        y = y+speed_y
        
        if y <0 or y >255:
                speed_y = speed_y*-1
                Lives += 1
                print(Lives)

        if x <0 or x >350:
                speed_x = speed_x*-1
                Lives += 1
                print(Lives)

        if Lives == 8 or Lives == 16 or Lives == 24 or Lives == 32 or Lives == 40 or Lives == 48:
                speed_x = speed_x*1.01
                speed_y = speed_y*1.01

        if Lives == 96:
                x = 200
                y = 200
                print ('Your pokeball has ran out of bounce')
                break


        #Order in which they go
        screen.fill((255, 255, 255))
        
        screen.blit(get_image('ball.png'), (x,y,20, 20))

        pygame.display.flip()
        clock.tick(60)

