import pygame
from config import *
from Code.player import*
from Code.floors import *
from Code.camera import *

class Screen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE)
        self.clock = pygame.time.Clock()
        self.poses = {
            'player':[0,0],
            'camera':[0,0]
        }

        self.createSprite()

    def createSprite(self):
        self.player = Player()
        self.floor  = floors()
        self.camera = Camera()

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
        self.floor.draw()
        self.player.draw()

    def update(self):
        self.camera.update(self.poses)
        self.player.update(self.poses)
        self.poses = {
            'player':self.player.pos,
            'camera':self.camera.position
        }
        self.floor.update(self.poses)