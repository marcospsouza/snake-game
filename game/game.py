import pygame
from pygame.locals import *
import pygame_menu
import time

from .objects.snake import Snake
from .objects.apple import Apple
from .objects.wall import Wall
from .utils.direction import Direction
from .handlers.eventHandler import EventHandler
from .handlers.colisionHandler import ColisionHandler

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = self.createSnake((0, 255, 0), 3)
        self.apple = self.createApple((255, 0, 0))
        self.drawWalls = True
        self.wall = self.createWall((128, 128, 128))
        self.direction = Direction.UP

    def setWalls(self, tuple, value):
        self.drawWalls = value

    def runGameMenu(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.menu = pygame_menu.Menu('Snake Game', 300, 300,
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
            self.updateElements()
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

    def updateElements(self):
        for i in range(len(self.snake.snakeBody)-1, 0, -1):
            self.snake.snakeBody[i] = (self.snake.snakeBody[i-1][0], self.snake.snakeBody[i-1][1])

        if self.direction == Direction.UP:
            self.snake.snakeBody[0] = (self.snake.snakeBody[0][0], self.snake.snakeBody[0][1] - 10)
        if self.direction == Direction.DOWN:
            self.snake.snakeBody[0] = (self.snake.snakeBody[0][0], self.snake.snakeBody[0][1] + 10)
        if self.direction == Direction.LEFT:
            self.snake.snakeBody[0] = (self.snake.snakeBody[0][0] - 10, self.snake.snakeBody[0][1])
        if self.direction == Direction.RIGHT:
            self.snake.snakeBody[0] = (self.snake.snakeBody[0][0] + 10, self.snake.snakeBody[0][1])
        
        if self.snake.snakeBody[0][0] < 0:
            self.snake.snakeBody[0] = (self.width-10, self.snake.snakeBody[0][1])
        if self.snake.snakeBody[0][0] > self.width:
            self.snake.snakeBody[0] = (10, self.snake.snakeBody[0][1])

        if self.snake.snakeBody[0][1] < 0:
            self.snake.snakeBody[0] = (self.snake.snakeBody[0][0], self.height-10)
        if self.snake.snakeBody[0][1] > self.height:
            self.snake.snakeBody[0] = (self.snake.snakeBody[0][0], 10)

    def createSnake(self, color, initialSize):
        return Snake(self, color, initialSize)

    def createApple(self, color):
        return Apple(self, color)

    def createWall(self, color):
        return Wall(self, color)