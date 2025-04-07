# main.py
import pygame
from game import Game

# Inicializar Pygame
pygame.init()

if __name__ == "__main__":
    game = Game()
    game.start()
    pygame.quit()
