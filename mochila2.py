from itertools import takewhile

'''
Este módulo implementa una serie de bloques de construcción de iteradores inspirados en construcciones de APL, Haskell y SML. Cada uno ha sido refundido en una forma adecuada para Python.

El módulo estandariza un conjunto básico de herramientas rápidas y eficientes en memoria que son útiles por sí mismas o en combinación. Juntos, forman un "álgebra de iteradores" que hace posible construir herramientas especializadas de forma sucinta y eficiente en Python puro.


'''


#Paquetes: "Nombre del paquete", Kilos, Precio
PAQUETES = (
    ("Paquete 1", 9, 150), 
    ("Paquete 2", 9, 160), 
    ("Paquete 3", 153, 200), 
    ("Paquete 4", 50, 160),
    ("Paquete 5", 15, 60), 
    ("Paquete 6", 66, 45), 
    ("Paquete 7", 27, 60), 
    ("Paquete 8", 39, 40),
    ("Paquete 9", 230, 591), 
    ("Paquete 10", 520, 10), 
    ("Paquete 11", 110, 70), 
    ("Paquete 12", 32, 30))

#Esta funcion retorna solo el valor convertido en flotante
def proceso_valor(item):
    nombre, peso, valor = item
    return float(valor)/ float(peso)

#Esta funcion toma el peso disponible de la mochila y le resta el peso que se le introduce por cada item
def proceso_peso(item):
    nombre, peso, valor = item
    proceso_peso.peso_maximo -= peso
    return proceso_peso.peso_maximo >= 0    

#carga máxima de la mochila
proceso_peso.peso_maximo = 500

'''
itertools.takewhile( predicado , iterable ) 
Haga un iterador que devuelva elementos de la iterable siempre que el predicado sea verdadero. Aproximadamente equivalente a:
'''

carga_lista = list(takewhile(proceso_peso, reversed(sorted(PAQUETES, key=proceso_valor))))

sumacarga = 0
sumavalor = 0

for item in carga_lista:
    print (item[0] + ' Peso :%i' % item[1] + ' valor :%i' % item[2])
    sumacarga = sumacarga + item[1]
    sumavalor = sumavalor + item[2]

print ('')
print ('Peso total paquetes: %i' % sumacarga)
print ('Valor total paquetes: %i' % sumavalor)