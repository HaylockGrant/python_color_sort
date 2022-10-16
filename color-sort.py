#this python script will take an array of colors and sort them in 2d by color distance using the CIEDE2000 algorithm
#using a window I'll generate all the colors as boids and use their color distance to determine their attraction to each other

import colorsys #for hsv to rgb conversion 
import math #for sqrt and pow
import random #for random numbers
# import CIEDE2000  #for color distance
# import colorMan #for color manipulation
#import local ciede2000.py
from ciede2000 import *
from colorMan import *

#initialize the colors
unsortedColors = ["ed8798", "d2c2dd", "f9d2db", "f7bfc1", "f4a88e", "b29260", "e93e50", "e73c4e", "8d135e", "6f307f", "8d4f92", "da2c93", "d3066b", "d6053e", "b81528", "b0131e", "e5321b", "ea5818", "ed5a15", "ef7510", "ed8a0b", "fbba00", "feed01", "e4e025", "f0e436", "faef73", "adc70b", "9cd320", "6cc12e", "7fb225", "a3c96d", "c5dda9", "e5eece", "f7ead9", "fee9d9", "ffffff", "daeeed", "cce8f0", "c8c8c8", "9B9B9B", "7c7e7c", "1071b1", "6397c6", "00a0d0", "00b0c7", "6fc8e6", "66b99b", "037f43", "008332", "006030", "005029", "003b24", "003020", "0c1514", "0b0b0b", "3e150f", "6e1e39", "731e25", "875a45", "82441f", "523b1b", "806E44", "645f25", "192120", "072432", "1b2451", "283067", "135086", "313c3f", "006376", "026e57"]

print (rgbtolab(105, 55, 137))
print (rgbtolab2(105, 55, 137))

print (CIEDE2000(rgbtolab(0, 0, 0), rgbtolab(255, 255, 255)))

#find the closest color to the first color in the array
nearestcolor = unsortedColors[1]
nearestcolorindex = 1
nearestcolorDistance = CIEDE2000(hextolab(unsortedColors[0]), hextolab(unsortedColors[1]))
for i in range(1,len(unsortedColors)):
    distance = CIEDE2000(hextolab(unsortedColors[0]), hextolab(unsortedColors[i]))
    if distance < nearestcolorDistance:
        nearestcolor = unsortedColors[i]
        nearestcolorindex = i
        nearestcolorDistance = distance

print (nearestcolor)