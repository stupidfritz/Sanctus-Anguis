import pygame, sys
from pygame.locals import *
import pipe

global window, window_width, window_height
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Thingy")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False

        window.fill((0, 0, 0))
        pipe.Pipe(window=window, width=20, height=100, color="green",
                  x_start=500, y_start=0)
        pygame.display.update()

pygame.quit()
sys.exit()
