"""
escriba un algoritmo en Python que implemente una funcion recursiva llamada 
contador_palabras que reciba tres parametros: 
un arreglo de palabras, la posicion inicial, y final del arreglo. 
La funcion deberá retornar el numero de palabras del arreglo.

Ejemplo:

texto="Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Nam arcu arcu, euismod mollis rhoncus quis, egestas at leo. 
Maecenas luctus neque nulla, vel imperdiet lacus ultrices vel. Mauris eget eros vel lacus molestie blandit."

Input
-------
contador_palabras(arreglo,0,longitud_del_arreglo)

Output
---------
34
Adjuntar archivo

"""

def contador_palabras(arreglo, ini, fin):
    if ini >= fin:
        return 0
    else:
        mid = (ini + fin) // 2
        return contador_palabras(arreglo, ini, mid) + contador_palabras(arreglo, mid + 1, fin) + 1

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam arcu arcu, euismod mollis rhoncus quis, egestas at leo. Maecenas luctus neque nulla, vel imperdiet lacus ultrices vel. Mauris eget eros vel lacus molestie blandit."
arreglo = texto.split()
resultado = contador_palabras(arreglo, 0, len(arreglo))
print(resultado)

