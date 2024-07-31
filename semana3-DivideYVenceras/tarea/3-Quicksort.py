"""
-   Implemente este algoritmo.
-   ¿Es un algoritmo “divide y vencerás”? Explique por qué
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2] 
    
    izq = []
    mid = []
    der = []
    
    for x in arr:
        if x < pivot:
            izq.append(x)
        elif x == pivot:
            mid.append(x)
        else:
            der.append(x)

    return quicksort(izq) + mid + quicksort(der)


arreglo = [2, 4, 6, 3, 1, 5, -99]
ordenado = quicksort(arreglo)
print("Arreglo ordenado crecientemente: ", ordenado)