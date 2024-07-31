#max y min tecnica clasica
#desordenar arreglo
def max_arr(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max


import random
def main():
    arr = list(range(30))
    random.shuffle(arr)
    print("Arreglo: ", arr)
    print("Maximo: ", max_arr(arr))
    
main()

#usando divide y venceras-------------------
def obtenerMin(arr, posInicial, posFinal):
    #dividimos el problema
    # problema = arreglo, conquista = minimo
    if (posInicial == posFinal):
        return arr[posInicial]
    else:
        mitad = (posInicial + posFinal) // 2 # el // me da la division entera
        minIzq = obtenerMin(arr, posInicial, mitad)
        minDer = obtenerMin(arr, mitad+1, posFinal) #si el medio es 12, el otro empieza en 13
        return minIzq if (minIzq < minDer) else minDer
    
def main():
    arr = [random.randint(1,200) for x in range(25)]
    print(arr)
    print("Min con DV: ", obtenerMin(arr, 0, len(arr)-1))

main()
