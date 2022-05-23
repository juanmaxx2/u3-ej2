from flores import Flor
import numpy as np
import csv
class Manejador:
    __Cantidad=None
    __Dimension=None
    __Incremento=None
    
    def __init__(self,dimension):
        self.__Flores=no.empty(dimension,dtype=Flor)
        self.__Cantidad=0
        self.__Dimension=dimension
    
    def AgregarFlor(self,unaFlor):
        if self.__Cantidad==self.__Dimension:
            self.__Dimension+=self.__Incremento
            self.__Flores.resize(self.__Dimension)
        self.__Flores[self.__cantidad]=unaFlor
        self.__cantidad+=1

    def Inicar(self):
        archivo=open('flores.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=False
            else:
                unaFlor=Flor(fila[0],fila[1],fila[2],fila[3])
                self.AgregarFlor(unaFlor)