#this class will initilize a window with boid circles as the colors in the array and will use the color distance to determine their attraction to each other
import pygame
import random
import math
from ciede2000 import *
from colorMan import *
from coloredBoid import *


#initialize the screen and display
pygame.init()

radius = 10

#initialize the colors
colors = ["ed8798", "d2c2dd", "f9d2db", "f7bfc1", "f4a88e", "b29260", "e93e50", "e73c4e", "8d135e", "6f307f", "8d4f92", "da2c93", "d3066b", "d6053e", "b81528", "b0131e", "e5321b", "ea5818", "ed5a15", "ef7510", "ed8a0b", "fbba00", "feed01", "e4e025", "f0e436", "faef73", "adc70b", "9cd320", "6cc12e", "7fb225", "a3c96d", "c5dda9", "e5eece", "f7ead9", "fee9d9", "ffffff", "daeeed", "cce8f0", "c8c8c8", "9B9B9B", "7c7e7c", "1071b1", "6397c6", "00a0d0", "00b0c7", "6fc8e6", "66b99b", "037f43", "008332", "006030", "005029", "003b24", "003020", "0c1514", "0b0b0b", "3e150f", "6e1e39", "731e25", "875a45", "82441f", "523b1b", "806E44", "645f25", "192120", "072432", "1b2451", "283067", "135086", "313c3f", "006376", "026e57"]

#calculate the size of the screen based on the number of colors
if(len(colors) < 1):
    print("Error: No colors found")
    exit()
n = (math.ceil((3+ math.sqrt((12*len(colors) -3)))/6)-1)*2 +1 #centered hexagon number formula to calculate the widest part of the hexagon
width = n*radius*2*2 #hexagon width times diameter times 2
height = width

screen = pygame.display.set_mode((width, height))
pygame.display.update()

#if the original width is too small then the window will resize automatically. To keep the window square we need to resize the height to match the width
if(pygame.display.Info().current_w > width):
    width, height = pygame.display.Info().current_w, pygame.display.Info().current_w
    pygame.display.set_mode((width, height))


#initilize boids
boids = []
for i in range(len(colors)):
    b = boid(colors[i], random.randint(radius, width-radius), random.randint(radius, height-radius), radius)
    for buddy in boids:
        while(b.areTouching(buddy)):
            b.x = random.randint(radius, width-radius)
            b.y = random.randint(radius, height-radius)
            print("buddy collision")
    boids.append(b)


#give each boid a random momentum and angle
for boid in boids:
    boid.momentum = random.randint(1,5)/10
    boid.angle = random.uniform(0, 2*math.pi)

#initilize clock
clock = pygame.time.Clock()
#main loop
running = True
screenfillColor = (0, 0, 0)    
while running:
    #input loop
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                pygame.quit()
                running = False
                break
            case pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    running = False
                    break
                #if keyboard space down, draw white
                if event.key == pygame.K_SPACE:
                    screenfillColor = (255, 255, 255)

                if event.key == pygame.K_UP:
                    for boy in boids:
                        boy.speedUp(0.1)

                if event.key == pygame.K_DOWN:
                    for boy in boids:
                        boy.slowDown(0.1)
            case pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    screenfillColor = (0, 0, 0)
    #check if game loop has been exited
    if not running:
        break
    #physics loop
    for boy in boids:
        otherboids = boids.copy()
        otherboids.remove(boy)
        for otherboid in otherboids: #commented out because it isn't finished
            if(boy.areTouching(otherboid)):
                boy.setAngle(boy.getAngleBetweenBoids(otherboid) + 180)
                otherboid.setAngle(otherboid.getAngleBetweenBoids(boy) + 180)
                touchingPersentage = boy.touchingPersentage(otherboid)
                boy.speedUp(1*touchingPersentage)
                otherboid.speedUp(1*touchingPersentage)
                boy.move()
                otherboid.move()
                boy.slowDown(1*touchingPersentage)
                otherboid.slowDown(1*touchingPersentage)
        #additional physics for boids
        boy.move()
        #boy.friction()
    #draw loop
    screen.fill(screenfillColor)
    for boy in boids:
        boy.draw(screen)
    pygame.display.update()
    clock.tick(30)