import pygame
from pygame.locals import *
import pygame_menu
import time

from .objects.snake import Snake
from .objects.apple import Apple
from .objects.wall import Wall
from .utils.direction import Direction
from .utils.color import Color
from .handlers.eventHandler import EventHandler
from .handlers.colisionHandler import ColisionHandler

class Game:
    def __init__(self, width, height, initialSnakeSize):
        self.width = width
        self.height = height
        self.initialSnakeSize = initialSnakeSize

        self.snake = Snake(width, height, Color.GREEN.value, initialSnakeSize)
        self.apple = Apple(width, height, Color.RED.value)
        self.wall = Wall(width, height, Color.GREY.value)
        self.drawWalls = True

        self.direction = Direction.UP

    def setWalls(self, tuple, value):
        self.drawWalls = value

    def runGameMenu(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.menu = pygame_menu.Menu('Snake Game', self.width, self.height,
                       theme=pygame_menu.themes.THEME_SOLARIZED)
        self.clock = pygame.time.Clock()
        self.menu.add.button('Play', self.runGame)        
        self.menu.add.selector('Walls: ', [('Yes', True), ('No', False)], onchange=self.setWalls)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)
        self.menu.mainloop(self.screen)

    def runGame(self):
        colisionHandler = ColisionHandler()
        eventHandler = EventHandler()
        while True:
            self.clock.tick(20)
            eventHandler.handleKeyboardEvents(self)
            colisionHandler.detectColisions(self)
            eventHandler.updateElements(self)
            self.drawElements(self.screen)

    def drawElements(self, screen):
        screen.fill((0,0,0))
        for snakeCell in self.snake.snakeBody:
            screen.blit(self.snake.snakeSkin, snakeCell)
        screen.blit(self.apple.appleSkin, self.apple.position)

        if self.drawWalls:
            for wallCell in self.wall.cells:
                screen.blit(self.wall.skin, wallCell)

        pygame.display.update()