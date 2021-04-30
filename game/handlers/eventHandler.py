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

    def updateElements(self, game):
        for i in range(len(game.snake.snakeBody)-1, 0, -1):
            game.snake.snakeBody[i] = (game.snake.snakeBody[i-1][0], game.snake.snakeBody[i-1][1])

        if game.direction == Direction.UP:
            game.snake.snakeBody[0] = (game.snake.snakeBody[0][0], game.snake.snakeBody[0][1] - 10)
        if game.direction == Direction.DOWN:
            game.snake.snakeBody[0] = (game.snake.snakeBody[0][0], game.snake.snakeBody[0][1] + 10)
        if game.direction == Direction.LEFT:
            game.snake.snakeBody[0] = (game.snake.snakeBody[0][0] - 10, game.snake.snakeBody[0][1])
        if game.direction == Direction.RIGHT:
            game.snake.snakeBody[0] = (game.snake.snakeBody[0][0] + 10, game.snake.snakeBody[0][1])
        
        if game.snake.snakeBody[0][0] < 0:
            game.snake.snakeBody[0] = (game.width-10, game.snake.snakeBody[0][1])
        if game.snake.snakeBody[0][0] > game.width:
            game.snake.snakeBody[0] = (10, game.snake.snakeBody[0][1])

        if game.snake.snakeBody[0][1] < 0:
            game.snake.snakeBody[0] = (game.snake.snakeBody[0][0], game.height-10)
        if game.snake.snakeBody[0][1] > game.height:
            game.snake.snakeBody[0] = (game.snake.snakeBody[0][0], 10)