import random
class NodonoTerminal:
    def __init__(self,nombre):
        self.reglas =[]
        self.nombre = nombre
        self.reglasPrima = []
        self.izquierdo = None
        self.derecho = None
    
    def __str__(self):
        return self.nombre
    
    def __repr__(self):
        return self.nombre

    def escogerCaminoAZar(self):
        sizeReglas = len(self.reglasPrima)
        posicionAzar = random.randint(0,sizeReglas-1)
        
        reglaAzar = self.reglasPrima[posicionAzar]
        if len(reglaAzar)==1:
            self.izquierdo = reglaAzar[0]
        else:
            self.izquierdo = reglaAzar[0]
            self.derecho = reglaAzar[1]
        
        
    
    def getIzquierdo(self):
        return self.izquierdo
    
    def getDerecho(self):
        return self.derecho