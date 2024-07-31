"""
Dado un texto t de n líneas, implementar un algoritmo “divide y vencerás” que cuente el número de palabras 
que contiene dicho texto.
Nota: Problema inicial para el algoritmo MapReduce de Google (fundamental e n Big Data).

texto = "Tres tristes tigren comen trigo en un trigal. Son felices, panzones y alegres"

output = 13
"""

def contador_palabras(arreglo, ini, fin):
    if ini >= fin:
        return 0
    else:
        mid = (ini + fin) // 2
        return contador_palabras(arreglo, ini, mid) + contador_palabras(arreglo, mid + 1, fin) + 1

texto = "Tres tristes tigres comen trigo en un trigal"
arreglo = texto.split()
resultado = contador_palabras(arreglo, 0, len(arreglo))
print(resultado)








