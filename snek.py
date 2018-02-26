import pygame
from pygame.locals import *


class Snek:
    def __init__(self, window, width, height, color, x, y):
        self.window = window
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y

        
        self.surface = pygame.display.get_surface()
        self.snek = pygame.Rect(self.x, self.y, self.width, self.height)
        self.surface.fill(Color(self.color), self.snek)
