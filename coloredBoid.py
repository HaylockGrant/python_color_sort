import pygame
import random
from ciede2000 import *
from colorMan import *
from hashTable import *

class boid:
    #static variables
    count = 0
    boids = []

    def degToRad(deg):
        return deg * math.pi / 180

    def radToDeg(rad):
        return rad * 180 / math.pi

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
    
    def getAngleBetweenBoids(self, boid):
        rad = math.atan2(boid.y - self.y, boid.x - self.x)
        if(rad < 0):
            rad += 2*math.pi
        return rad

    def getDistanceBetweenBoids(self, boid):
        return math.sqrt((boid.x - self.x)**2 + (boid.y - self.y)**2)
    
    def areTouching(self, boid):
        return self.getDistanceBetweenBoids(boid) <= self.radius + boid.radius

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
