class Color:

    #CONSTRUCTOR
    def __init__ (self, rojo, verde, azul):
        self.__rojo = rojo
        self.__verde = verde
        self.__azul = azul

    #GETTERS
    def getRojo(self):
        return self.__rojo

    def getVerde(self):
        return self.__verde

    def getAzul(self):
        return self.__azul

    #SETTER
    def setRojo(self, rojo):
        self.__rojo = rojo

    def setVerde(self, verde):
        self.__verde = verde

    def setAzul(self, azul):
        self.__azul = azul


    #METODOS
    def detalleColor(self):
        print("Rojo: ", self.__rojo, "\nVerde: ", self.__verde, "\nAzul: ", self.__azul)

    