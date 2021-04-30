import pygame

class Wall:
    def __init__(self, width, height, color):
        self.skin = pygame.Surface((10, 10))
        self.skin.fill(color)
        self.cells = []

        for x in range(width):
            for y in range(height):
                if (x == 0 or x == 10 or x == width-10 or x == width-20):
                    self.cells.append((x, y))                    
                if (y == 0 or y == 10 or y == width-10 or y == width-20):
                    self.cells.append((x, y)) 