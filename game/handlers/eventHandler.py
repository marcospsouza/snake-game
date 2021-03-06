import pygame
from pygame.locals import *
from ..utils.direction import Direction

class EventHandler:
    
    def handleKeyboardEvents(self, game):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                key = event.key
                if (key == K_UP or key == K_w) and game.direction != Direction.DOWN:
                    game.direction = Direction.UP
                if (key == K_DOWN or key == K_s) and game.direction != Direction.UP:
                    game.direction = Direction.DOWN
                if (key == K_LEFT or key == K_a) and game.direction != Direction.RIGHT:
                    game.direction = Direction.LEFT
                if (key == K_RIGHT or key== K_d) and game.direction != Direction.LEFT:
                    game.direction = Direction.RIGHT
                if key == K_ESCAPE:
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