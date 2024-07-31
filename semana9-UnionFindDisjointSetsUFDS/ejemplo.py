print("HOLA MUNDO DEL PROBLEMA ANTERIOR CALCULAREMOS LA CANTIDAD")
print("DE ALUMNOS QUE APROBARON Y REPROBARON")

import numpy as np

# Crear un arreglo vacío para almacenar las notas
a = np.zeros(4)

for i in range(4):
    s = input(f"Ingrese el nombre del alumno {i + 1}: ")
    x = float(input(f"Ingrese la nota de {s}: "))
    a[i] = x

print("\nLAS NOTAS DE LOS ALUMNOS")
print(a)

aprobados = reprobados = 0

for i in a:
    if i >= 11:
        aprobados += 1
        print(f"El alumno aprobó con una nota de {i}")
    else:
        print(f"El alumno reprobó con una nota de {i}")
        reprobados += 1

print("\nLOS ALUMNOS QUE APROBARON FUERON", aprobados)
print("LOS ALUMNOS QUE REPROBARON FUERON", reprobados)

