class Flor:
    __Nombre=None
    __Numero=None
    __Color=None
    __Descripcion=None

    def __init__(self,Numero,Nombre,Color,Descripcion):
        self.__Nombre=Nombre
        self.__Numero=Numero
        self.__Color=Color
        self.__Descripcion=Descripcion
    
    def getNombre(self):
        return self.__Nombre