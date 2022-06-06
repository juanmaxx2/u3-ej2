from flor import Flor
import numpy as np
import csv
class ManejadorFlor:
    __Cantidad=None
    __Dimension=None
    __Incremento=None
    
    def __init__(self,dimension=5):
        self.__Flores=np.empty(dimension,dtype=Flor)
        self.__Cantidad=0
        self.__Dimension=dimension
    
    def AgregarFlor(self,unaFlor):
        if self.__Cantidad==self.__Dimension:
            self.__Dimension+=self.__Incremento
            self.__Flores.resize(self.__Dimension)
        self.__Flores[self.__Cantidad]=unaFlor
        self.__Cantidad+=1

    def Iniciar(self):
        archivo=open('flores.csv')
        reader=csv.reader(archivo,delimiter=',')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=False
            else:
                unaFlor=Flor(fila[0],fila[1],fila[2],fila[3])
                self.AgregarFlor(unaFlor)
        archivo.close()
    
    def retFlor(self,i):
        return self.__Flores[i-1]

    def getNombreF(self,i):
        return self.__Flores[i].getNombre()
    
    def retFlor(self,i):
        return self.__Flores[i]
    
    def getFlorN(self):
        return self.__Flores.getNombre()