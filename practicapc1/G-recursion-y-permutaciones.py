""" [MISMO ENUNCIADO QUE ANTES SÓLO QUE AHORA SON COMBINACIONES]
Utilizando la técnica de recursión:

Implementa una función (recursiva) que reciba como parámetro un entero positivo N
e imprima todas las combinaciones (en cualquier orden) de números entre 1 y N cuya suma sea N

ej:
N: 5

Respuestas:
    { 5 },
    { 1, 4 },
    { 2, 3 },
    { 1, 1, 3 },
    { 1, 2, 2 },
    { 1, 1, 1, 2 },
    { 1, 1, 1, 1, 1 }

N: 4

Respuestas:
    { 4 },
    { 1, 3 },
    { 2, 2 },
    { 1, 1, 2 },
    { 1, 1, 1, 1 }
"""

def combinaciones(n):
    arr = []
    combinacionesSuma(n, arr, 1)

def combinacionesSuma(n, arr, start):
    if n == 0:
        print(arr)
        return
    for i in range(start, n + 1):
        if i <= n:
            arr.append(i)
            combinacionesSuma(n - i, arr, i)
            arr.pop()

combinaciones(4)