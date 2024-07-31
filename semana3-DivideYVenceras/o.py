def validar(reinas, N, nivel):

  #print("En funcion validar ", "reinas: ", reinas, "N=", N, "nivel=", nivel)

  i = 0 #columna a recorrer

  while (i < nivel):

    # RESTRICCIONES

    # Validamos que las reinas no esten en la misma fila o en la misma columna => (reinas[i] == reinas[nivel])

    # Validamos que las reinas no esten en la misma diagonal => (abs(nivel - i) == abs(reinas[nivel] - reinas[i]))

    if ((reinas[i] == reinas[nivel]) or (abs(nivel - i) == abs(reinas[nivel] - reinas[i]))):

      return False

    i = i + 1

  return True



contX = 0



def nReinas(reinas, N, nivel, cont):

  # Caso Base para la recursividad: Todas las reinas colocadas en el arreglo (tablero) y validadas

  if (nivel == N): #Nivel del Arbol == Numero de Reinas

    global contX

    contX = contX + 1

    print("Solucion ", contX, " : ")

    print("reinas[]: ", reinas)

    print()



  # Seguimos buscando las reinas por colocar => 

  # 1) Validamos las posiciones

  # 2) Ejecutamos nuevamente (incluye volver atrás en el nivel o columna)

  else:

    # Recorre el Nivel (o columna del Tablero), para validar que no se "coman" entre las reinas

    print ("nivel = ", nivel, ", reinas[nivel] = ", reinas[nivel], " N = ", N)

    reinas[nivel] = 0 #Ubicamos a la Reina en la primera fila (0) de la columna "nivel"

    while(reinas[nivel] < N): #Mientras no pasemos de la ultima fila, de la columna "nivel"

      if (validar(reinas, N, nivel)): #Validamos que no se "coman" las reinas

        nReinas(reinas, N, nivel + 1, cont) #Recursividad: Pasamos al siguiente nivel del arbol (siguiente columna del Tablero)

      reinas[nivel] = reinas[nivel] + 1 #Pasamos a la siguiente fila





##################

###    main    ###

##################

def main():

  nivel = 0   # Nivel en el Arbol (o columna en el Tablero)

  N = 4       # Numero de Reinas por defecto

  N = int(input("Ingresar la cantidad de reinas : "))



reinas = []

for i in range(int(N)):

    reinas.append(-1) #Incializamos el arreglo con -1, porque aun no hay reinas ubicadas



nReinas(reinas, N, nivel, 0)



main()