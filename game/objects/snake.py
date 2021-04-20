import pygame
import random

class Snake:
    def __init__(self, gameInstance, color, initialSize):
        self.snakeSkin = pygame.Surface((10, 10))
        self.snakeBody = []
        self.snakeSkin.fill(color)
        
        initialPositionX = random.randint(100, gameInstance.width - 100)//10 * 10
        initialPositionY = random.randint(100, gameInstance.height - 100)//10 * 10

        for i in range (initialSize):
            self.snakeBody.append((initialPositionX, initialPositionY + (i*10)))

