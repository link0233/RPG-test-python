from config import *

def getCameraPosition():
    with open("./Code/poses/camera.pos",'r') as f:
        for t in f:
            cPos = t.strip().split(',')
            cPos[0] = int(cPos[0])
            cPos[1] = int(cPos[1])
            break
    return cPos