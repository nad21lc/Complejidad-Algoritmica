def digitoAletras(digito):
    if digito == '2':
        return 'ABC'
    elif digito == '3':
        return 'DEF'
    elif digito == '4':
        return 'GHI'
    elif digito == '5':
        return 'JKL'
    elif digito == '6':
        return 'MNO'
    elif digito == '7':
        return 'PQRS'
    elif digito == '8':
        return 'TUV'
    elif digito == '9':
        return 'WXYZ'
    else:
        return ''

def generarCombinacionDeLetras(digitos):
    if not digitos:
        return []

    queue = [""]
    
    for digito in digitos:
        letras = digitoAletras(digito)
        if not letras:
            return ["NO"]
        
        combinaciones = []
        for combinacion in queue:
            for letra in letras:
                combinaciones.append(combinacion + letra)
        queue = combinaciones

    return queue


with open("historial_marcacion.txt", "r") as file:
    lineas = file.readlines()


for linea in lineas:
    digitos = linea.strip().split()
    resultado = generarCombinacionDeLetras(digitos)
    if resultado == ["NO"]:
        print(resultado[0])
    else:
        print(resultado)
        
        
#Se optó por usar el algoritmo BFS para generar todas las posibles combinaciones. 

# Esta elección se hizo en lugar de DFS (Depth-First Search) 
# debido a la forma en que BFS explora todas las opciones a la misma "profundidad" 
# antes de avanzar a la siguiente. 
# Siendo la "profundidad" el número de dígitos procesados en la secuencia de entrada. 
# Por lo tanto, BFS asegura que todas las combinaciones se generen en el orden apropiado, 
# primero todas las combinaciones de un solo dígito, 
# seguidas de todas las combinaciones de dos dígitos, y así sucesivamente.
