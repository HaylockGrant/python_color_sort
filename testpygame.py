#create a simple square pygame window
import pygame

pygame.init()
screen = pygame.display.set_mode((200, 200))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    if not running:
        break
    pygame.display.update()