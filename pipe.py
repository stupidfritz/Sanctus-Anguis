import pygame, random
from pygame.locals import *


class Pipe:
    def __init__(self, window, width=20, height=random.randint(50, 400), color="red",
                 x_start=500, y_start=10):
        self.width = width
        self.height = height
        self.color = color
        self.window = window
        self.x_pos = x_start
        self.y_pos = y_start
        
        self.shade = pygame.display.get_surface()
        self.up = pygame.Rect(self.x_pos,self.y_pos,self.width,self.height)
        self.down = pygame.Rect(self.x_pos,self.height+100,self.width,500)
        self.shade.fill(Color(color), self.up)
        self.shade.fill(Color(color), self.down)
