class Point:

    #CONSTRUCTOR
    # poniendo valores por defecto asi se puede crear un objeto sin tener que pasarle parametros.
    def __init__ (self, puntoX = None, puntoY = None):
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


