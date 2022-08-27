import pygame
from config import *
from Code.floor import *

class floors:
    def __init__(self):
        self.floorGroup = pygame.sprite.Group()
        path = './image/Floors/'
        self.images = {
            'grass':pygame.image.load(path+'grass.png').convert_alpha()
        }
        #Floor('grass',self.floorGroup,(0,0),self.images)
        self.surface  = pygame.display.get_surface()

        self.floorsPos=[]

    def draw(self):
        self.floorGroup.draw(self.surface)

    def update(self):
        self.floorGroup.update()
        #get palyer position
        with open('./Code/poses/player.pos') as f:
            for t in f:
                pPos = t.strip().split(',')
                break
        pPos = (int(pPos[0])//100,int(pPos[1])//100)
        #createfloor
        dd = 0
        kk = self.floorsPos
        for floorPos in self.floorsPos:
            distance = int(((abs(pPos[0]-floorPos[0]))**2+(abs(pPos[1]-floorPos[1]))**2)**(0.5))
            if distance>DELETE_DISTANCE:
                del kk[dd]
            
        self.floorsPos = kk
        for a in range(DELETE_DISTANCE//3*2):
            for b in range(DELETE_DISTANCE//3*2):
                pos = (a+pPos[0]-DELETE_DISTANCE//6*2,b+pPos[1]-DELETE_DISTANCE//6*2)
                if pos not in self.floorsPos:
                    self.floorsPos.append(pos)
                    Floor('grass',self.floorGroup,pos,self.images)