"""
Utilizando la técnica de backtracking:

Implemente una función que imprima para un arreglo de tamaño N todos los posibles
arreglo con valores del 1 al 9 en cada celda.

ej:
    N = 2
    Respuestas:
    
    [1, 1]
    [1, 2]
    [1, 3]
    [1, 4]
    [1, 5]
    [1, 6]
    [1, 7]
    [1, 8]
    [1, 9]
    [2, 1z]
    [2, 2]
    [2, 3]
    [2, 4]
    [2, 5]
    [2, 6]
    [2, 7]
    [2, 8]
    [2, 9]
    ...
    [9, 9]
"""

def imprimirArr(n):
    arreglo = []
    backtracking(arreglo, n)
    
def backtracking(arr, n):
    if len(arr) == n:
        print(arr)
        return 0
    
    for i in range(1,10):
        arr.append(i)
        backtracking(arr,n)
        arr.pop()
        
imprimirArr(2)