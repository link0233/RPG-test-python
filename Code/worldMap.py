from config import*

class worldMap:
    def __init__(self,data):
        self.map = []
        if data['Map'] == 'create':
            for a in range(0,WORLD_SIZE[1]+2):
                c = []
                for b in range(0,WORLD_SIZE[0]+2):
                    if a == 0 or a == WORLD_SIZE[1]+1 or b == 0 or b == WORLD_SIZE[0]+1:
                        c.append(['grass',False])
                    else:
                        c.append(['grass',True])
                
                self.map.append(c)
        else:
            self.map = data["Map"]
        