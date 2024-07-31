"""
Escriba un algoritmo en Python que implemente una función recursiva, 
que reciba como parametro un número n>0, y devuelva 
la suma de los dobles de los números desde 1 a n (ambos incluidos).

Ejemplo:

Input

n = 4

DobleSuma (n)

Output

20

(equivale a 2*1+2*2+2*3+2*4)

Adjuntar archivo
"""

def sumaDoble(n, ini=1):
    if ini > n:
        return 0
    print(ini*2)
    return (ini*2) + sumaDoble(n, ini+1)

print("Suma: " + str(sumaDoble(4)))

