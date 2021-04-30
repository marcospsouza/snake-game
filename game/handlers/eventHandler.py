import pygame
from pygame.locals import *
from ..utils.direction import Direction

class EventHandler:
    
    def handleKeyboardEvents(self, game):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_UP and game.direction != Direction.DOWN:
                    game.direction = Direction.UP
                if event.key == K_DOWN and game.direction != Direction.UP:
                    game.direction = Direction.DOWN
                if event.key == K_LEFT and game.direction != Direction.RIGHT:
                    game.direction = Direction.LEFT
                if event.key == K_RIGHT and game.direction != Direction.LEFT:
                    game.direction = Direction.RIGHT
                if event.key == K_ESCAPE:
                    game.runGameMenu()