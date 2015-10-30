# DRAWING STUFF

# import pygame

import pygame
import sys

# initialize pygame

pygame.init()

# set colors

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# create window

window = pygame.display.set_mode((800,600))

window.fill(blue)

# window name - ?


# treat background as an array of pixels

Pix = pygame.PixelArray(window)

Pix[200][200] = white


# draw line, circle, rectangle, polygon

pygame.draw.line(window, red, (200,300), (500,500), 5)         # 5 - thickness in pixels

pygame.draw.circle(window, red, (400,300), 100, 50)            # center coordinates, radius, thickness

pygame.draw.rect(window, red, (100,100, 200,300))               # top left x,y,  width,  height

pygame.draw.polygon(window, white, ((50,50),(200,16),(300,70),(400,125), (300, 200)))           # all point coords. a Tupil of tupils





# LOOP:

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()                        # main line !!!



# close program

pygame.quit()

quit()