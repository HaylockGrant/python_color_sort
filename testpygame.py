#create a simple square pygame window
#import pygame
from coloredBoid import *
from hashTable import *
# pygame.init()
# screen = pygame.display.set_mode((200, 200))
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 running = False
#     if not running:
#         break
#     pygame.display.update()
# pygame.quit()
boida = boid("ffffff", 0, 0, 10)
boidb = boid("000000", 0, 0, 10)
print(boida.getDistanceBetweenBoids(boidb))
print(boida.getAngleBetweenBoids(boidb))
print(boidb.getAngleBetweenBoids(boida))