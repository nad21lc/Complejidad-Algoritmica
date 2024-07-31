"""
Escriba un algoritmo en Python que implemente una función recursiva 
que reciba como parámetro una cadena, y la devuelva de manera inversa, 
comenzando desde el último carácter hasta el primero.
"""

def invertirCadena(cadena):
    if len(cadena) < 1:
        return cadena
    
    return cadena[-1] + invertirCadena(cadena[:-1])
    

print(invertirCadena("HelloKitty"))