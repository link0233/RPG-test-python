import pygame
import json
from config import *
from Code.player import*
from Code.floors import *
from Code.camera import *
from Code.worldMap import *

class Screen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE)
        self.clock = pygame.time.Clock()
        self.poses = {
            'player':[0,0],
            'camera':[0,0]
        }

        self.loadSave()
        self.createSprite()

    def createSprite(self):
        self.map = worldMap(self.data)
        self.player = Player()
        self.floor  = floors()
        self.camera = Camera()
        self.data["Map"] = self.map.map

    def gameloop(self):
        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.Savegame()
                    import sys;sys.exit()

            self.update()
            self.draw()

            pygame.display.update()

    def draw(self):
        self.screen.fill((0,0,0))
        self.floor.draw()
        self.player.draw()

    def update(self):
        self.camera.update(self.data)
        self.player.update(self.data)
        self.data['player'] = self.player.pos
        self.data['camera'] = self.camera.position
        self.floor.update(self.data)

    def loadSave(self):
        self.data = {
            'player':[0,0],
            'camera':[0,0],
            'Map' : 'create'
        }
        # with open ('./save/map.rt','w') as f:
        #     json.dump(self.data,f)
        with open('./save/map.json') as f:
            dd = json.load(f)
            print(dd)
            self.data = dd

    def Savegame(self):
        with open('./save/map.json' , 'w') as f:
            json.dump(self.data,f)