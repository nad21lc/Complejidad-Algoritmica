"""
Utilizando la técnica de recursión:

Dado un número entero N, retorna el valor de la suma del doble de cada número desde N hasta 1.

ej.
    N = 4
    Respuesta: (4 * 2) + (3 * 2) + (2 * 2) + (1 * 2) = 20
"""

def sumaDoble(n):
  if n == 0:
    return 0
  print(n*2)
  return (n*2) + sumaDoble(n-1)

print("Resultado: " + str(sumaDoble(4)))
# Output: 20