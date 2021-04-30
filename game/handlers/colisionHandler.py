
from ..utils.direction import Direction
from ..objects.snake import Snake
from ..objects.apple import Apple

import random

class ColisionHandler():

    def newApplePosition(self, game):
        return (random.randint(100, game.width - 100)//10 * 10, 
                    random.randint(100, game.height - 100)//10 * 10)

    def detectAppleColision(self, game):
        if game.apple.position == game.snake.snakeBody[0]:
            game.apple.position = self.newApplePosition(game)
            game.snake.snakeBody.append([0,0])

    def detectWallColision(self, game):        
        if game.drawWalls and game.snake.snakeBody[0] in game.wall.cells:     
            game.snake = Snake(game.width, game.height, (0, 255, 0), 3)
            game.apple = Apple(game.width, game.height, (255, 0, 0))
            game.direction = Direction.UP
            game.runGameMenu()

    def detectSnakeColision(self, game):      
        for i in range(len(game.snake.snakeBody)):
            for j in range(len(game.snake.snakeBody)):
                if i != j and game.snake.snakeBody[i] == game.snake.snakeBody[j]:       
                    game.snake = Snake(game.width, game.height, (0, 255, 0), 3)
                    game.apple = Apple(game.width, game.height, (255, 0, 0))
                    game.direction = Direction.UP
                    game.runGameMenu()
                    break

    def detectColisions(self, game):
        self.detectAppleColision(game)
        self.detectWallColision(game)
        self.detectSnakeColision(game)