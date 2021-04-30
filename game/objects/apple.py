import pygame
import random

class Apple:
    def __init__(self, width, height, color):
        self.appleSkin = pygame.Surface((10, 10))
        self.appleSkin.fill(color)
        self.position = (random.randint(100, width - 100)//10 * 10, random.randint(100, height - 100)//10 * 10)
