import numpy as np
from specs import Specs
from component import Component
from utilities import *
from scipy.linalg import solve 


class Net():
    
    def __init__(self):
        self.n_nodes=0
        self.components=[]
        self.kcl=[]

    def import_file(self,filename):
        with open(filename,"r") as netfile:
            header=netfile.readline()
            if(not header.startswith(Specs.header())):
            #DA DEFINIRE UN CUSTOM ERROR
                raise EOFError
            else:
                #pick the number of nodes of the circuit (to not count them)
                self.n_nodes=int(header.replace(Specs.header(),""))
                juice=netfile.readlines()
                for line in juice[:-1]:
                    com=Component()
                    com.from_fileline(line)
                    self.components.append(com)
                  
    def __str__(self):
        return "<Net object>\nNodes:{}".format(self.n_nodes)


    def solve(self):
        #to add modified analysis 
        if(self.n_nodes<=0):
            print("Empty or corrupted net, please load it first!")
            raise EOFError
        else:
            self.kcl=nodalMatrix(self.n_nodes)
            for index,com in enumerate(self.components):
                #keep in mind that index start form one: otherwise we leave the zero without sign
                self.kcl[com.connections[0]].append(-1*(index+1))
                self.kcl[com.connections[1]].append(index+1)
            print(self.kcl)
            #print(self.components[0].connections)
            #now we have to explicit the current in every component
            #let's create cases
            self.descriptorMatrix=np.zeros((self.n_nodes-1,self.n_nodes-1),dtype=np.float64)
            self.costantTerms=np.zeros((self.n_nodes-1,1),dtype=np.float64)
            for index,kcl in enumerate(self.kcl[1:]):
                for com_index in kcl:
                    com=self.components[abs(com_index)-1]
                    sign=com_index/abs(com_index)
                    if com.type is 'R':         
                        self.descriptorMatrix[index,com.connections[1]-1]+=(pow(com.value,-1))*sign
                        if(com.connections[0] is not 0):
                            self.descriptorMatrix[index,com.connections[0]-1]-=(pow(com.value,-1))*sign
                    if com.type is 'I':
                        self.costantTerms[index,0]+=(com.value*sign)
            print(self.descriptorMatrix)
            print(self.costantTerms)
            self.solutions=solve(self.descriptorMatrix,self.costantTerms)
            print(self.solutions)

if __name__=="__main__":
    net=Net()
    net.import_file("ex2.nt")
    #print(net.components[4])
    net.solve()