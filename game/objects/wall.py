import pygame

class Wall:
    def __init__(self, gameInstance, color):
        self.skin = pygame.Surface((10, 10))
        self.skin.fill(color)
        self.cells = []

        for x in range(gameInstance.width):
            for y in range(gameInstance.height):
                if (x == 0 or x == 10 or x == gameInstance.width-10 or x == gameInstance.width-20):
                    self.cells.append((x, y))                    
                if (y == 0 or y == 10 or y == gameInstance.width-10 or y == gameInstance.width-20):
                    self.cells.append((x, y)) 