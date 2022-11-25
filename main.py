import pygame
import sys
import random


pygame.init()

screen = pygame.display.set_mode((576, 1024))

background = pygame.image.load("").convert()
background = pygame.transform.scale2x(background)
 
fish = 
pygame.image.load
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background,(0,0))
    pygame.display.update()









