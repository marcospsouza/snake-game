import pygame
import random

class Apple:
    def __init__(self, gameInstance, color):
        self.appleSkin = pygame.Surface((10, 10))
        self.appleSkin.fill(color)
        self.position = (random.randint(100, gameInstance.width - 100)//10 * 10, random.randint(100, gameInstance.height - 100)//10 * 10)
