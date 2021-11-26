import pygame
from pygame.locals import *
import pygame_vkeyboard
from pygame_vkeyboard import *
import pygame_assets as assets

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Spot the difference: NIGHTMARE MODE')

running = True
while running:
   for event in pygame.event.get():
     if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            running = False
        elif event.type == QUIT:
            running = False


# Let's code a game in python!
## for Github gamejam


### Based on a single topic: "Bug"
### Most annoying game (ie: Unbeatable games, don't touch the button, invisible path, overcomplex games- dnd/pathfinder stressful games)
## Why will people play this: Masochism, "numbers go up", unlock everything/completionist
## we need: achievements/milestones easter eggs/secret or hidden content
## game ideas: minigames 
      # pin the tail on the invisible pony.
      # guess the next number sequences (Except half of it is unsolveable)(you can do this one with dictoinaries)
      # spot the difference (1 pixel changed)
      # lights out games (initial conditions unsolveable)
      