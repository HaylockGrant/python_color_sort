#this class will initilize a window with boid circles as the colors in the array and will use the color distance to determine their attraction to each other
import pygame
import random
import math
from ciede2000 import *
from colorMan import *

#initialize the screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
