import pygame

#physics loop
def doPhysics():
    return True
    #this function will calculate the physics of the boids

#draw loop, this class will draw the boids to the screen and update the screen. it may not always be necessary to update the screen if the physics loop did not change anything
def doDraw():
    pygame.display.update()
    #this function will draw the boids to the screen after the physics loop