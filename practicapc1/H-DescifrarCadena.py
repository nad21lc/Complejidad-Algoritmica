"""

Escriba un algoritmo en Python que implemente una una función llamada descifrar(cadena),
que reciba como parámetro una cadena de caracteres (contraseña) con una longitud máxima de 10 caracteres 
y muestre todas las combinaciones realizadas hasta descifrar el texto ingresado.

Ejemplo:

Input

cadena = oculto/123

descifrar(cadena)

Output

o

oc

ocu

ocul

ocult

oculto

oculto/

oculto/1

oculto/12

oculto/123

- Indique que tecnica utilizó para la implementación

"""

# def descifrar(cadena):
#     generar_combinaciones(cadena, '')

# def generar_combinaciones(restante, parcial):
#     if len(parcial) > 0:
#         print(parcial)

#     if len(restante) == 0:
#         return

#     for i in range(len(restante)):
#         generar_combinaciones(restante[i+1:], parcial + restante[i])
        

def descifrar(cadena):
    tem = []
    generarCombinaciones(cadena, tem)

def generarCombinaciones(cadena, temArr, lon=0):
    if lon >= len(cadena):
        return
    letra = cadena[lon]
    temArr.append(letra)
    print(''.join(temArr))
    generarCombinaciones(cadena, temArr, lon + 1)
    temArr.pop() 

cadena = "oculto/123"
descifrar(cadena)




# def descifrar(cadena):
#     generar_combinaciones(cadena)

# def generar_combinaciones(cadena, lon=0):
#     if lon >= len(cadena):
#         return
#     print(cadena[lon])
#     return cadena[0] + generar_combinaciones(cadena, lon+1)
    

# cadena = "oculto/123"
# descifrar(cadena)


