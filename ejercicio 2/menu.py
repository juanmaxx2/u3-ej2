import manejador import Manejador
class Menu:
    __opcion=None

    def __init__(self):
        self.__opcion=0

    def Iniciar(self):
    unManejador=Manejador()
    while self.__opcion!='3':
        print()
        print()
        print('salir')
        self.__opcion=input('elija la opcion')

        if self.__opcion=='1':
        elif self.__opcion=='2':
