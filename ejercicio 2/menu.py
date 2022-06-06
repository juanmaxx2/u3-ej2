from manejadorFlores import ManejadorFlor
from manejadorRamos import ManejadorRamo
class Menu:
    __opcion=None

    def __init__(self):
        self.__opcion=0

    def Iniciar(self):
        ManejadorR=ManejadorRamo()
        ManejadorF=ManejadorFlor()
        ManejadorF.Iniciar()
        while self.__opcion!='3':
            print('\n1.Anadir Ramo')
            print('2.Mostrar flores mas pedidas:')
            print('3.Buscar flores por ramo')
            print('4.Salir')
            self.__opcion=input('elija la opcion:')

            if self.__opcion=='1':
                ManejadorR.addFlor(ManejadorF)
            elif self.__opcion=='2':
                ManejadorR.BuscarFlores(ManejadorF)
            elif self.__opcion=='3':
                ramo=input('ingrese el tramanio del ramo a buscar:')
                ManejadorR.BuscarporTamaño(ManejadorF,ramo)