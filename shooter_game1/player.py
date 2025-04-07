
import pygame
from character import Character

class Player(Character):
    def __init__(self, x, y, image):
        super().__init__(x, y, image, lives=3)
        self.score = 0

    def move(self, keys):
        if keys[pygame.K_LEFT]: self.x -= 5
        if keys[pygame.K_RIGHT]: self.x += 5
        if keys[pygame.K_UP]: self.y -= 5
        if keys[pygame.K_DOWN]: self.y += 5