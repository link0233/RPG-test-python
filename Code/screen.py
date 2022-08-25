import pygame
from config import *
from Code.player import*

class Screen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE)
        self.clock = pygame.time.Clock()

        self.createSprite()

    def createSprite(self):
        self.player = Player()

    def gameloop(self):
        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    import sys;sys.exit()

            self.update()
            self.draw()

            pygame.display.update()

    def draw(self):
        self.screen.fill((0,0,0))
        self.player.draw()

    def update(self):
        self.player.update()