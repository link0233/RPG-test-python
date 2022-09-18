from logging import PlaceHolder
import pygame
from config import *
#from function import getCameraPosition

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.group = pygame.sprite.Group()
        super().__init__(self.group)
        self.image = pygame.Surface((SPRITE_SIZE,SPRITE_SIZE))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREENSIZE[0]//2,SCREENSIZE[1]//2)

        self.load_image()

        self.vector2 = pygame.math.Vector2()
        self.type = 'walk'
        self.rotate = 2
        self.pos = [0,0]

        self.screen = pygame.display.get_surface()

    def update(self,pos):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] or key[pygame.K_UP]:
            self.rotate = 0
            self.vector2.y = float(-1)
        elif key[pygame.K_s] or key[pygame.K_DOWN]:
            self.rotate = 2
            self.vector2.y = 1
        else:
            self.vector2.y = 0

        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.rotate = 3
            self.vector2.x = float(-1)
        elif key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.rotate = 1
            self.vector2.x = 1
        else:
            self.vector2.x = 0

        #move
        if self.vector2.magnitude() > 0:
            self.vector2 = self.vector2.normalize()
        # if self.pos[0]>-WORLD_SIZE[0]//2*SPRITE_SIZE-SPRITE_SIZE//2 and self.pos[0]<WORLD_SIZE[0]//2*SPRITE_SIZE+SPRITE_SIZE//2 and self.pos[1]>-WORLD_SIZE[1]*SPRITE_SIZE//2-SPRITE_SIZE//2 and self.pos[1]<WORLD_SIZE[1]//2*SPRITE_SIZE+SPRITE_SIZE//2:
        self.pos[0] += self.vector2.x*PLAYER_MOVESPEED
        self.pos[1] += self.vector2.y*PLAYER_MOVESPEED

        #cpos = getCameraPosition()
        cpos = pos['camera']
        self.rect.centerx = self.pos[0]-cpos[0]+SCREENSIZE[0]//2
        self.rect.centery = self.pos[1]-cpos[1]+SCREENSIZE[1]//2

        #set image
        self.image = self.images[self.type][self.rotate]
        self.image.set_colorkey((255,255,255))

        

        # with open('./Code/poses/player.pos','w') as f:
        #     f.write(str(self.pos[0])+','+str(self.pos[1]))
    def draw(self):
        #screen = pygame.display.get_surface()
        self.group.draw(self.screen)

    def load_image(self):
        walk_path = "./image/player/walk/"
        self.images = {
            'walk':[pygame.image.load(walk_path+"up.png").convert_alpha(),pygame.image.load(walk_path+"right.png").convert_alpha(),pygame.image.load(walk_path+"down.png").convert_alpha(),pygame.image.load(walk_path+"left.png").convert_alpha()]
        }