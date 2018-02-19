import pygame, sys, random, time
from pygame.locals import *
import pipe

global window, window_width, window_height
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Thingy")
level = random.randint(50, 450)
level2 = random.randint(50, 450)
level3 = random.randint(50, 450)
running = True
clock = pygame.time.Clock()


pos1 = 800
pos2 = 800
pos3 = 800

change = 525
change2 = 525
r = 0
g = 150
b = 200

while running:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False
    clock.tick(30)
    
    window.fill((r, g, b))
    
    pos1 -= 4
    
        
    pipe.Pipe(window=window, width=40, height=level,
              color="green", x_start=pos1, y_start=0)
    pipe.Pipe(window=window, width=40, height=level2,
              color="green", x_start=pos2, y_start=0)
    pipe.Pipe(window=window, width=40, height=level3,
              color="green", x_start=pos3, y_start=0)

    if pos1 <= 1:
        pos1 = 800
    if pos1 == 800:
        level = random.randint(50, 450)
    if pos1 <= change:
        pos2 -= 4
        change += 4
    if pos2 <= change2:
        pos3 -= 4
        change2 += 4
    if pos2 <= 1:
        level2 = random.randint(50, 450)
        pos2 = 800
    if pos3 <= 1:
        pos3 = 800
        level3 = random.randint(50, 350)
    if change >= 800:
        change = 800
    if change2 >= 800:
        change2 = 800
        
   

    pygame.display.update()

pygame.quit()
sys.exit()
