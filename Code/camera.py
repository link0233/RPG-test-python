from config import *

class Camera:
    def __init__(self):
        self.position = [0,0]
        with open('./Code/poses/camera.pos','w') as f:
            f.write('0,0')
    
    def update(self):
        with open('./Code/poses/player.pos','r') as f:
            for t in f:
                pPos = t.strip().split(',')
                break
        pPos = (float(pPos[0]),float(pPos[1]))
        if abs(self.position[0]-pPos[0])>PLAYER_MOVESPEED:
            if self.position[0]>pPos[0]:
                self.position[0]-=PLAYER_MOVESPEED
            else:
                self.position[0]+=PLAYER_MOVESPEED
        
        if abs(self.position[1]-pPos[1])>PLAYER_MOVESPEED:
            if self.position[1]>pPos[1]:
                self.position[1]-=PLAYER_MOVESPEED
            else:
                self.position[1]+=PLAYER_MOVESPEED

        with open('./Code/poses/camera.pos','w') as f:
            f.write(str(self.position[0])+','+str(self.position[1]))