"""
Utilizando la técnica de recursión:

Dada una lista que puede contener números enteros u otras listas (que pueden contener números enteros
u otras listas con las mismas condiciones), determine la suma total de todos los números enteros.

ej.
    Números: [[[1]], [[[[4]]]], 7, 0, [[2, 3], 5, [3, 2]]]
    Respuesta: 1 + 4 + 7 + 0 + 2 + 3 + 5 + 3 + 2 = 27

    Números: [1, 1, 1, 1, [2, [3], [4], [0, -8]]]
    Respueta: 5
"""

def dameSuma(arreglo):
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
    
    return recursion(0, arreglo)

print(dameSuma([[[1]], [[[[4]]]], 7, 0, [[2, 3], 5, [3, 2]]]))
# Output: 27

print(dameSuma([1, 1, 1, 1, [2, [3], [4], [0, -8]]]))
# Output: 5