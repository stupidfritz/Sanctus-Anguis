import pygame
from pygame.locals import *


class Snek:
    def __init__(self, window, width, height, color, x, y):
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y
        self.surface = pygame.display.get_surface()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


        
    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 5
        if key[pygame.K_DOWN]:
            if self.y<600:
                self.y += dist
        if key[pygame.K_UP]:
            if self.y<6:
                self.y -= dist
        if key[pygame.K_RIGHT]:
            if self.x<800:
                self.x += dist
        if key[pygame.K_LEFT]:
            if self.x>6:
                self.x -= dist
    def draw(self):
        self.surface.fill(self.color, self.rect)

    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)
