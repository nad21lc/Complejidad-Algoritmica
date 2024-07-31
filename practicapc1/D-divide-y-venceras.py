"""
Utilizando la técnica de divide y vencerás:

Implementar una función para cada una de las siguientes operaciones
- Máximo elemento de un arreglo
- Mínimo elemento de un arreglo
- Suma de todos los elementos de un arreglo
- Multiplicación de todos los elementos de un arreglo
--Division de todos los elementos de un arreglo
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


#obtener minimo
def obtenerMin(arreglo, i, j):
    if i==j:
        return arreglo[i]
    else:
        mitad =(i+j) // 2 # // es para que salga entero
        minIzq = obtenerMin(arreglo, i, mitad)
        minDer = obtenerMin(arreglo, mitad+1, j)
        if minIzq < minDer:
            return minIzq
        else:
            return minDer


#Suma de todos los elementos de un arreglo 
def obtenerSumaElementos(arreglo, i, j):
    if i==j:
        return arreglo[i]
    else:
        mitad =(i+j) // 2 # // es para que salga entero
        midIzq = obtenerSumaElementos(arreglo, i, mitad)
        midDer = obtenerSumaElementos(arreglo, mitad+1, j)
        return midIzq + midDer


#Multiplicación de todos los elementos de un arreglo
def obtenerMultiplicacionElementos(arreglo, i, j):
    if i==j:
        return arreglo[i]
    else:
        mitad =(i+j) // 2 # // es para que salga entero
        midIzq = obtenerMultiplicacionElementos(arreglo, i, mitad)
        midDer = obtenerMultiplicacionElementos(arreglo, mitad+1, j)
        return midIzq*midDer


#Division de todos los elementos de un arreglo
def obtenerDivisionElementos(arreglo, i, j):
    if i==j:
        return arreglo[i]
    else:
        mitad =(i+j) // 2 # // es para que salga entero
        midIzq = obtenerDivisionElementos(arreglo, i, mitad)
        midDer = obtenerDivisionElementos(arreglo, mitad+1, j)
        return (midIzq/midDer)

arreglo = [2, 4, 6, 3, 1, 5, -99]

print("Maximo con divide y venceras: ", obtenerMax(arreglo, 0, len(arreglo)-1))
print("Minimo con divide y venceras: ", obtenerMin(arreglo, 0, len(arreglo)-1))
print("Suma de todos los elementos: ", obtenerSumaElementos(arreglo, 0, len(arreglo)-1))
print("Multiplicación de todos los elementos: ", obtenerMultiplicacionElementos(arreglo, 0, len(arreglo)-1))
print("División de todos los elementos: ", obtenerDivisionElementos(arreglo, 0, len(arreglo)-1))