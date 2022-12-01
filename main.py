import pygame 
import sys
import random

def game_floor():
  screen.blit(floor_base,(floor_x_pos,900))


        
pygame.init()
clock = pygame.time.Clock()
#variables
gravity = 3
bird_movement = 0
screen = pygame.display.set_mode((576,1024))


#The while true allows the screen to stay open while the game runs O.B.
background = pygame.image.load("imgs/bg.png").convert()
#Scale background to fit screen 
background = pygame.transform.scale2x(background) 

bird = pygame.image.load("imgs/bird2.png").convert_alpha()
bird = pygame.transform.scale2x(bird) 
bird_rect = bird.get_rect(center=(100,512))

floor_base = pygame.image.load("imgs/base.png").convert()
floor_base = pygame.transform.scale2x(floor_base) 
floor_x_pos = 0

while True:

  for event in pygame.event.get():
#define how to exit the game O.B.
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        bird_movement = 0
        bird_movement -= 12
        bird_rect.center = (100,512)
        
  screen.blit(background, (0,0))

  bird_movement += gravity
  bird_rect.centery += gravity
  screen.blit(bird, (100, bird_movement))

  #Create Floor
  floor_x_pos -= 1
  game_floor()
  
  pygame.display.update()
  clock.tick(120)









