#this class will initilize a window with boid circles as the colors in the array and will use the color distance to determine their attraction to each other
import pygame
import random
import math
from ciede2000 import *
from colorMan import *

#initialize the screen and display
pygame.init()
#in the future, the screen size will be determined by the number of boids.  For now, it is a fixed size
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

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
                    redraw = True
            case pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    screen.fill((0,0,0))
                    redraw = True
    if(doPhysics() or redraw): #the physics loop returns true if there was an update to the screen
        doDraw()



#physics loop
def doPhysics():
    return True
    #this function will calculate the physics of the boids

#draw loop, this class will draw the boids to the screen and update the screen. it may not always be necessary to update the screen if the physics loop did not change anything
def doDraw():
    pygame.display.update()
    #this function will draw the boids to the screen after the physics loop

