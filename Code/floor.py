import pygame
from config import *

class Floor(pygame.sprite.Sprite):
    def __init__(self,type,floors,pos,images):
        super().__init__(floors)
        self.type = type
        self.image = images[type]
        self.image = pygame.transform.scale(self.image,(SPRITE_SIZE,SPRITE_SIZE))
        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos[0] * SPRITE_SIZE,self.pos[1] * SPRITE_SIZE)

    def update(self):
        #get payer pos
        with open('./Code/poses/player.pos') as f:
            for t in f:
                pPos = t.strip().split(',')
                break
        pPos = (int(pPos[0])//100,int(pPos[1])//100)

        distance = int(((abs(pPos[0]-self.pos[0]))**2+(abs(pPos[1]-self.pos[1]))**2)**(0.5))
        if distance>DELETE_DISTANCE:
            self.kill()