"""
Escriba un algoritmo en Python que implemente una función recursiva que reciba como parámetro 
una lista conteniendo ya sea ítems de números enteros y sublistas de enteros, 
y devuelva la suma total de todos los ítems.

Ejemplo:

Input

lista = [1, 2, [3,4], [5,6] ]

SumaEnterosdeLista (lista) 

Output

21

(equivale a (1+2) + (3+4) + (5+6))
"""

def dameSumaTotal(arreglo):
    print(recursion(0, arreglo))

def recursion(indice, arreglo):
    tam = len(arreglo)
    if indice >= tam:
        return 0
    respuesta = 0
    if type(arreglo[indice]) == list:
        respuesta = recursion(0, arreglo[indice])
    else:
        respuesta = arreglo[indice]   
    return respuesta + recursion(indice + 1, arreglo)

lista = [1, 2, [3,4], [5,6]]
dameSumaTotal(lista)