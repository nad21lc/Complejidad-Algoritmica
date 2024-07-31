"""
-   Escriba un algoritmo “simple” para calcular este problema.
-   Escriba un algoritmo “divide y vencerás” para calcular este problema
"""

#Obtener máximo
def obtenerMax(arreglo, i, j):
    if i==j:
        return arreglo[i]
    else:
        mitad =(i+j) // 2 # // es para que salga entero
        midIzq = obtenerMax(arreglo, i, mitad)
        midDer = obtenerMax(arreglo, mitad+1, j)
        if midIzq > midDer:
            return midIzq
        else:
            return midDer


arreglo = [2, 4, 6, 3, 1, 5, -99]     
print("Maximo con divide y venceras: ", obtenerMax(arreglo, 0, len(arreglo)-1))