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
        self.ringForBlack = False
        self.ringForWhite = False
        if(CIEDE2000(hextolab(self.color), hextolab("000000")) < 2.5):
            self.ringForBlack = True
        if(CIEDE2000(hextolab(self.color), hextolab("ffffff")) < 2.5):
            self.ringForWhite = True
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
    
    def getAngleBetweenBoids(self, buddy): #returns the angle between the boids as degrees
        rad = math.atan2(buddy.y - self.y, buddy.x - self.x)
        if(rad < 0):
            rad += 2*math.pi
        return boid.radToDeg(rad)

    def getMomentum(self):
        return self.momentum

    def setMomentum(self, momentum):
        self.momentum = momentum

    def getAngle(self):
        return boid.radToDeg(self.angle)

    def setAngle(self, angle):
        ang = boid.degToRad(angle)
        while(ang > 2*math.pi):
            ang -= 2*math.pi
        while(ang < 0):
            ang += 2*math.pi
        self.angle = ang


    def getDistanceBetweenBoids(self, boid): #returns the distance between the boids
        return math.sqrt((boid.x - self.x)**2 + (boid.y - self.y)**2)
    
    def areTouching(self, boid): #returns true if the boids are touching
        return self.getDistanceBetweenBoids(boid) <= self.radius + boid.radius

    def touchingPersentage(self, boid): #returns the persentage of the boids that are touching
        distance = self.getDistanceBetweenBoids(boid)
        return 1 - (distance/(self.radius + boid.radius))

    #draw the boid to the screen
    def draw(self, screen, invert = False):
        if(not invert and self.ringForBlack):
            pygame.draw.circle(screen, hextorgb("2d2d2d"), (self.x, self.y), self.radius+1)
        if(invert and self.ringForWhite):
            pygame.draw.circle(screen, hextorgb("d2d2d2"), (self.x, self.y), self.radius+1)
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

    def rotateClockwise(self, degrees):
        angle = boid.degToRad(degrees)
        self.angle += angle
        while(self.angle > 2*math.pi):
            self.angle -= 2*math.pi
        return self.angle

    def rotateCounterClockwise(self, degrees):
        angle = boid.degToRad(degrees)
        self.angle -= angle
        while(self.angle < 0):
            self.angle += 2*math.pi
        return self.angle

    def combineVelocity(self, momentum, angle):
        while angle > 360:
            angle -= 360
        while angle < 0:
            angle += 360
        angle = boid.degToRad(angle)
        self.momentum = math.sqrt(self.momentum**2 + momentum**2 - 2*self.momentum*momentum*math.cos(self.angle - angle))
        self.angle = math.atan2(self.momentum*math.sin(self.angle - angle), self.momentum*math.cos(self.angle - angle) + momentum)

    def slowDown(self, amount):
        self.momentum -= amount
        if self.momentum < 0:
            self.momentum = 0

    def speedUp(self, amount):
        self.momentum += amount


