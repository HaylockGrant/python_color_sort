import pygame
import random
from ciede2000 import *
from colorMan import *
from hashTable import *

class boid:
    #static variables
    count = 0
    boids = []

    def __init__(self, color, x, y, radius):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.momentum = 0
        self.angle = 0
        self.distanceMap = HashTable(1)
        for buddy in boid.boids:
            buddy.distanceMap.set_val(self, self.calculateColorDifferance(buddy))
            self.distanceMap.set_val(buddy, self.calculateColorDifferance(buddy))
        boid.boids.append(self)
        boid.count += 1

    #draw the boid to the screen
    def draw(self, screen):
        pygame.draw.circle(screen, hextorgb("000000"), (self.x, self.y), self.radius+1)
        pygame.draw.circle(screen, hextorgb(self.color), (self.x, self.y), self.radius)
    
    def calculateColorDifferance(self, boid):
        return CIEDE2000(hextolab(self.color), hextolab(boid.color))

    def findColorDistance(self, boid):
        return self.distanceMap.get_val(boid)

    def move(self):
        #bounce off walls
        if(self.x < self.radius):
            self.x = self.radius
            self.angle = math.pi - self.angle
        if(self.x > pygame.display.Info().current_w - self.radius):
            self.x = pygame.display.Info().current_w - self.radius
            self.angle = math.pi - self.angle
        if(self.y < self.radius):
            self.y = self.radius
            self.angle = -self.angle
        if(self.y > pygame.display.Info().current_w - self.radius):
            self.y = pygame.display.Info().current_w - self.radius
            self.angle = -self.angle
        #move boid
        self.x += self.momentum * math.cos(self.angle)
        self.y += self.momentum * math.sin(self.angle)

    def degToAngle(deg):
        return (deg % 360)/360 * math.pi * 2

    def angleToDeg(angle):
        return angle/(math.pi * 2) * 360