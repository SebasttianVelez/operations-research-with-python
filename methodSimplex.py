'''

PRIMER EJERCICIO
--------------------------------------

funcion objetivo:
Minimizar f(x) = 70(x1) + 80(x2) + 85(x3)

x1 + x2 + x3 = 999

sujeto a:
x1 + 4(x2) + 8(x3) <= 4500
40(x1) + 30(x2) + 20(x3) <= 36000
3(x1) + 2(x2) + 4(x3) <= 2700

--------------------------------------
restriccion o bounds
x >= 0

--------------------------------------

'''
from scipy.optimize import linprog

coeficientes = [70, 80, 85]

argumentosDesigualdad = [[1,4,8], [40,30,20], [3,2,4]]

resultadosDesigualdad = [4500, 36000, 2700]

argumentosIgualdad = [[1,1,1]]

resultadosIgualdad = [999]

resultado = linprog(coeficientes, argumentosDesigualdad, resultadosDesigualdad, argumentosIgualdad, resultadosIgualdad, bounds=(0, None))


print("\n Primer Ejercicio: ")

print ("valor optimo", round(resultado.fun))
print ("\nX(1):", round(resultado.x[0]))
print ("\nX(2):", round(resultado.x[1]))
print ("\nX(3):", round(resultado.x[2]))



'''
Ejercicio #2:  
Ahora las desigualdades tienen signo contrario, por lo tanto multiplicamos los coeficientes *(-1)

Minimizar: w = 430(y1) + 460(y2) + 420(y3)

sujeto a:

y1 + 3(y2) + y3 >= 3
2(y1) + 4(y3) >= 2
y1 + 2(y2) >= 5

bounds
y1, y2, y3 >=0

SOLUCION OPTIMA:

y1 = 1, y2 = 2, y3 = 0, w = 1350


'''


coeficientes2 = [430, 460, 420] 

argumentosDesigualdad2 = [[-1,-3,-1], [-2,0,-4], [-1,-2,0]]

resultadosDesigualdad2 = [-3, -2, -5]


resultado2 = linprog(coeficientes2, argumentosDesigualdad2, resultadosDesigualdad2, bounds=(0, None))
print("\n Segundo Ejercicio: ")
print ("valor optimo", round(resultado2.fun))
print ("\nX(1):", round(resultado2.x[0]))
print ("\nX(2):", round(resultado2.x[1]))
print ("\nX(3):", round(resultado2.x[2]))