import pygame
from pygame.locals import *
import pygame_menu
import random
import time

from .objects.snake import Snake
from .objects.apple import Apple
from .objects.wall import Wall
from .utils.direction import Direction

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
        while True:
            self.clock.tick(20)
            self.handleEvents()
            self.detectColisions()
            if self.direction != 0:
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
    
    def detectColisions(self):
        if self.apple.position == self.snake.snakeBody[0]:
            self.apple.position = (random.randint(100, self.width - 100)//10 * 10, random.randint(100, self.height - 100)//10 * 10)
            self.snake.snakeBody.append([0,0])
        
        for i in range(len(self.snake.snakeBody)):
            for j in range(len(self.snake.snakeBody)):
                if i != j and self.snake.snakeBody[i] == self.snake.snakeBody[j]:       
                    self.snake = self.createSnake((0, 255, 0), 3)
                    self.apple = self.createApple((255, 0, 0))
                    self.direction = Direction.UP
                    self.runGameMenu()
                    break
        
        if self.drawWalls and self.snake.snakeBody[0] in self.wall.cells:     
            self.snake = self.createSnake((0, 255, 0), 3)
            self.apple = self.createApple((255, 0, 0))
            self.direction = Direction.UP
            self.runGameMenu()

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

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_UP and self.direction != Direction.DOWN:
                    self.direction = Direction.UP
                if event.key == K_DOWN and self.direction != Direction.UP:
                    self.direction = Direction.DOWN
                if event.key == K_LEFT and self.direction != Direction.RIGHT:
                    self.direction = Direction.LEFT
                if event.key == K_RIGHT and self.direction != Direction.LEFT:
                    self.direction = Direction.RIGHT
                if event.key == K_ESCAPE:
                    self.runGameMenu()

    def createSnake(self, color, initialSize):
        return Snake(self, color, initialSize)

    def createApple(self, color):
        return Apple(self, color)

    def createWall(self, color):
        return Wall(self, color)