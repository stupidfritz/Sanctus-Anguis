import pygame
from pygame.locals import *
pygame.font.init()


class Menu:
    def __init__(self, window, size, message, x, y, color):
        self.size = size
        self.window = window
        self.message = message
        self.x = x
        self.y = y
        self.color = color

        self.thing = pygame.font.SysFont('Comic Sans MS', self.size)

        self.text = self.thing.render(self.message, False, self.color)

        self.render = self.window.blit(self.text, (self.x, self.y))

        
        
