class Point:

    #CONSTRUCTOR
    def __init__ (self, puntoX, puntoY):
        self.__puntoX = puntoX
        self.__puntoY = puntoY


    #GETTER
    def getPuntoX(self):
        return self.__puntoX
        
    def getPuntoY(self):
        return self.__puntoY
    
    #SETTER
    def setPuntoX(self,  puntoX):
        self.__puntoX = puntoX
        
    def setPuntoY(self, puntoY):
        self.__puntoY = puntoY

    #METODOS        
    def detallePoin(self):
        print("Punto X: ", self.__puntoX , "\nPunto Y: ", self.__puntoY)


