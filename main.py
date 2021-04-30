import configparser
from game.game import Game

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')
    width = int(config['DEFAULT']['width'])
    height = int(config['DEFAULT']['height'])
    snakeSize = int(config['DEFAULT']['initialSnakeSize'])

    game = Game(width, height, snakeSize)
    game.runGameMenu()