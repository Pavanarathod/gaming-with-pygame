import pygame
import time
from pygame.locals import *

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg")
        self.x = 100
        self.y = 100
        self.direction = 'down'

    def draw(self):
        self.parent_screen.fill((110, 110, 5))
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()

    def moove_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def moove_up(self):
        self.direction = 'up'

    def mooe_down(self):
        self.direction = 'down'

    def walk(self):
        if self.direction == 'left':
            self.x -= 10
        if self.direction == 'right':
            self.x += 10
        if self.direction == 'up':
            self.y -= 10
        if self.direction == 'down':
            self.y += 10

        self.draw()

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))
        self.surface.fill((33, 207, 79))
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        run = False
                    if event.key == K_UP:
                        self.snake.moove_up()
                    if event.key == K_DOWN:
                        self.snake.mooe_down()
                    if event.key == K_LEFT:
                        self.snake.moove_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                if event.type == QUIT:
                    run = False
            self.snake.walk()
            time.sleep(0.2)

if __name__ == '__main__':
    game = Game()
    game.run()
