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

tableMap = HashTable(1)
tableMap.set_val("red", (255, 0, 0))
tableMap.set_val("green", (0, 255, 0))
tableMap.set_val("blue", (0, 0, 255))

print(tableMap.get_val("red"))
print(tableMap.get_val("green"))
print(tableMap.get_val("blue"))
print(tableMap.get_val("purple"))
