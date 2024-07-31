"""
Utilizando la técnica de fuerza bruta:

Dado un arreglo de números, imprime todos los posibles pares de números cuya suma sea igual a X.
  ej: 
    Arreglo: [1, 2, 3, 4, 5, 6, 8]
    X: 9

    Respuestas:
      1 8
      3 6
      4 5
"""

def imprimirNumSumaIgualInput(arreglo, n):
  respuesta = []
  for i in range(len(arreglo)):
    primer_numero = arreglo[i]
    for j in range(i+1, len(arreglo)):
      segundo_numero = arreglo[j]
      if (primer_numero+segundo_numero) == n:
        respuesta.append([primer_numero,segundo_numero])
  return respuesta
  
print(imprimirNumSumaIgualInput([1, 2, 3, 4, 5, 6, 8], 9))

print(imprimirNumSumaIgualInput([5, 5, 10, 0, 14, 15, 20, -5], 10))
  