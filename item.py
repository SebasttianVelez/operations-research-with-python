

class Elemento:
    def __init__(self, id, peso, beneficio):
        self.id = id
        self.peso = peso
        self.beneficio=beneficio
    
    def getId(self):
        return self.id
    
    def getPeso(self):
        return self.peso
    
    def getBeneficio(self):
        return self.beneficio

class Mochila:
    def __init__(self, capacidad, elementos):
        self.capacidad = capacidad
        self.elementos = elementos

    def getCapacidad(self):
        return self.capacidad

    def llenarElementos(self, elementos):
        for i in range(self.capacidad):
            self.elementos.append(elementos[i])

    def getElementos(self):
        return self.elementos
    
    def imprimirElementos(self):
        for elemento in self.elementos:
                print(elemento.getId(),end=" - ")
                print(elemento.getPeso(),end=" - ")
                print(elemento.getBeneficio()) 



# Elementos:


elementos =[Elemento("A", 1, 2),Elemento("B", 2, 5), Elemento("C", 4, 6), Elemento("D", 5, 10), Elemento("E", 7, 13), Elemento("F", 8, 16)]

mochila = Mochila(8, elementos)
mochila.imprimirElementos()

