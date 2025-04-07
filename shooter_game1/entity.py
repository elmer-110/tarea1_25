import pygame

class Entity:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def move(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
