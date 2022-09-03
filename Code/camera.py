from config import *

class Camera:
    def __init__(self):
        self.position = [0,0]
        # with open('./Code/poses/camera.pos','w') as f:
        #     f.write('0,0')
    
    def update(self,pos):
        # with open('./Code/poses/player.pos','r') as f:
        #     for t in f:
        #         pPos = t.strip().split(',')
        #         break
        pPos = pos['player']
        if abs(self.position[0]-pPos[0])>PLAYER_MOVESPEED:
            if self.position[0]>pPos[0] and self.position[0]>-WORLD_SIZE[0]//2*SPRITE_SIZE:
                self.position[0]-=PLAYER_MOVESPEED
            elif self.position[0]<WORLD_SIZE[0]//2*SPRITE_SIZE and self.position[0]<pPos[0]:
                self.position[0]+=PLAYER_MOVESPEED
            
        if abs(self.position[1]-pPos[1])>PLAYER_MOVESPEED:
            if self.position[1]>pPos[1] and self.position[1]>-WORLD_SIZE[1]//2*SPRITE_SIZE:
                self.position[1]-=PLAYER_MOVESPEED
            elif self.position[1]<WORLD_SIZE[1]//2*SPRITE_SIZE and self.position[1]<pPos[1]:
                self.position[1]+=PLAYER_MOVESPEED
        # with open('./Code/poses/camera.pos','w') as f:
        #     f.write(str(self.position[0])+','+str(self.position[1]))