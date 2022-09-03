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
        self.floors = []

    def draw(self):
        self.floorGroup.draw(self.surface)

    def update(self,Pos):
        #self.floorGroup.update()
        #get palyer position
        # with open('./Code/poses/player.pos','r') as f:
        #     for t in f:
        #         pPos = t.strip().split(',')
        #         break
        # pPos = (int(float(pPos[0]))//100,int(float(pPos[1]))//100)
        pPos = Pos['player']
        #createfloor
        dd = 0
        kk = self.floorsPos
        for floorPos in self.floorsPos:
            distance = int(((abs(pPos[0]//SPRITE_SIZE-floorPos[0]))**2+(abs(pPos[1]//SPRITE_SIZE-floorPos[1]))**2)**(0.5))
            if distance>DELETE_DISTANCE//3*2:
                del kk[dd]
            
        self.floorsPos = kk
        for a in range(DELETE_DISTANCE):
            for b in range(DELETE_DISTANCE):
                pos = (a+pPos[0]//SPRITE_SIZE-DELETE_DISTANCE//2,b+pPos[1]//SPRITE_SIZE-DELETE_DISTANCE//2)
                if pos not in self.floorsPos:
                    self.floorsPos.append(pos)
                    newFloor = Floor('grass',self.floorGroup,pos,self.images)
                    self.floors.append(newFloor)

        for floor in self.floors:
            floor.update(Pos)