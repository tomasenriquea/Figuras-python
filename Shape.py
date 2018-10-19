from abc import ABCMeta, abstractmethod
# asi se crea una clase abstracta

class Shape(metaclass = ABCMeta):
    def __init__(self, codigo, nombre, edad):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def saludad():
        pass
        
        
    




  