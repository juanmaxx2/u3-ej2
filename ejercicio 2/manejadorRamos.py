from ramo import Ramo
class ManejadorRamo:
    __Lista=[]

    def __init__(self):
        self.__Lista=[]

    def addFlor(self,ManejadorF):
        num=int(input('\ningrese la catidad de flores del ramo:'))
        if num<=4 and num>=1:
            tam=input('ingrese el tamanio del ramo:')
            print('las flores disponibles son:\n1){}\n2){}\n3){}\n4){}\n5){}'.format(ManejadorF.getNombreF(0),ManejadorF.getNombreF(1),ManejadorF.getNombreF(2),ManejadorF.getNombreF(3),ManejadorF.getNombreF(4)))
            for i in range(num):
                ramo=Ramo(tam)
                flor=int(input('\nIngrese la flor numero {}:'.format(i+1)))
                if flor>0 and flor<6:
                    ramo.addFlor(ManejadorF.retFlor(flor))
            self.__Lista.append(ramo)
        else:print('el tamanio no esta permitido')
        

    def BuscarFlores(self,ManejadorF):
        lista2=[0,0,0,0,0]
        for i in range(len(self.__Lista)):
            for j in range(len(self.__Lista[i].getFlor())):
                if self.__Lista[i].getFlor()[j].getNombre()==ManejadorF.getNombreF(0):
                    lista2[0]+=1
                elif self.__Lista[i].getFlor()[j].getNombre()==ManejadorF.getNombreF(1):
                    lista2[1]+=1
                elif self.__Lista[i].getFlor()[j].getNombre()==ManejadorF.getNombreF(2):
                    lista2[2]+=1
                elif self.__Lista[i].getFlor()[j].getNombre()==ManejadorF.getNombreF(3):
                    lista2[3]+=1
                elif self.__Lista[i].getFlor()[j].getNombre()==ManejadorF.getNombreF(4):
                    lista2[4]+=1
                else: print('g')
        for i in range(len(lista2)):
            print(lista2[i])

    def BuscarporTamaño(self,ManejadorF,unramo):
        i=0
        while unramo!=self.__Lista[i].getTamanio():
            i+=1
        if unramo==self.__Lista[i].getTamanio():
            print(self.__Lista[i].getFlor())