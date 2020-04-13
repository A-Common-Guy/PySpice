from utilities import mapper
class Component():
    def __init__(self):
        self.topology=[]
        self.type=None
        self.value=0
        self.connections=[]
    

    def from_fileline(self,line):
        #print(line)
        self.topology=line.split()
        #print(self.topology)
        self.value=self.topology.pop()
        self.type=self.topology.pop()
        self.topology=list(map(int,self.topology))
        self.value=int(self.value)
        for i in range(len(self.topology)):
            if(self.topology[i] is 1):
                self.connections.append(i)

    
    
    def __str__(self):
        return "<Component object>\nCurrent value:{}\nType:{}".format(self.value,mapper[self.type])

                