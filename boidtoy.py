#this class will initilize a window with boid circles as the colors in the array and will use the color distance to determine their attraction to each other
import pygame
import random
import math
from ciede2000 import *
from colorMan import *
from coloredBoid import *


#initialize the screen and display
pygame.init()

radius = 25
#initilize boids
boids = []
#white boid at the center of the screen for testing
boids.append(boid(("ffffff"), round(width/2), round(height/2), radius))

#calculate the size of the screen based on the number of boids
n = (math.ceil((3+ math.sqrt((12*len(boids) -3)))/6)-1)*2 +1
width = n*radius*2
height = width

screen = pygame.display.set_mode((width, height))



#initilize clock
clock = pygame.time.Clock()

running = True
while running:
    #main game loop
    redraw = False
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
                    screen.fill((255,255,255))
            case pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    screen.fill((0,0,0))
    #check if game loop has been exited
    if not running:
        break
    
    #physics loop
    
    #draw loop
    for boid in boids:
        boid.draw(screen)
    
    pygame.display.update()
    clock.tick(30)