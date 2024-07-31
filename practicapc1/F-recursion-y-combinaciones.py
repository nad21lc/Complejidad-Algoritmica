"""
Utilizando la técnica de recursión:

Implementa una función (recursiva) que reciba como parámetro un entero positivo N
e imprima todas las PERMUTACIONES (en cualquier orden) de números entre 1 y N cuya suma sea N

ej:
    N: 4

Respuestas:
    { 1, 1, 1, 1 },
    { 1, 1, 2 },
    { 1, 2, 1 },
    { 2, 1, 1 }
    { 1, 3 },
    { 3, 1 }
    { 2, 2 }
    { 4 }
"""

def combinaciones(n):
    arr = []
    combinacionesSuma(n, arr)

def combinacionesSuma(n, arr, suma=0):
    if suma == n:
        print(arr)
    else:
        for i in range(1, n+1):
            suma += i
            if suma <= n:
                arr.append(i)
                combinacionesSuma(n, arr, suma)
                arr.pop()
            suma -= i


combinaciones(4)
