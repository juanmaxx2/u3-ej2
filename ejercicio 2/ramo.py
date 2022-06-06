class Ramo:
    __Tamanio=None
    __Flor=[]

    def __init__(self,tamanio):
        self.__Flor=[]
        self.__Tamanio=tamanio

    def addFlor(self,flor):
        self.__Flor.append(flor)
    
    def getTamanio(self):
        return self.__Tamanio
 
    def getFlor(self):
        return self.__Flor
    
    def getFlor1(self,i):
        return self.__Flor[i]
    
    def getCantF(self):
        c=0
        for i in range(len(self.__Flor)):
            c+=1
        return c