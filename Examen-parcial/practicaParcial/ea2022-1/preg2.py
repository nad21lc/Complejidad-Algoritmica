def encontrar_orden_de_bebidas(N, bebidas, M, relaciones):
    # Construir un grafo dirigido que represente las relaciones entre las bebidas
    grafo = {}
    for bebida in bebidas:
        grafo[bebida] = []

    for _ in range(M):
        B1, B2 = relaciones.pop(0)
        grafo[B1].append(B2)

    # Función para realizar un recorrido topológico en el grafo
    def recorrido_topologico(grafo, nodo, visitado, resultado):
        visitado.add(nodo)
        for vecino in grafo[nodo]:
            if vecino not in visitado:
                recorrido_topologico(grafo, vecino, visitado, resultado)
        resultado.append(nodo)

    # Realizar el recorrido topológico para encontrar el orden óptimo
    orden_optimo = []
    visitado = set()

    for bebida in bebidas:
        if bebida not in visitado:
            recorrido_topologico(grafo, bebida, visitado, orden_optimo)

    orden_optimo.reverse()

    return orden_optimo

# Función para procesar un caso de prueba
def procesar_caso_prueba(numero_caso):
    N = int(input())
    bebidas = [input() for _ in range(N)]
    M = int(input())
    relaciones = [input().split() for _ in range(M)]

    orden_optimo = encontrar_orden_de_bebidas(N, bebidas, M, relaciones)

    print(f"Caso #{numero_caso}: usted debería tomar las bebidas en éste orden: {' '.join(orden_optimo)}.")
    print()

# Procesar múltiples casos de prueba
numero_caso = 1
while True:
    if numero_caso == 4:
        break
    procesar_caso_prueba(numero_caso)
    numero_caso += 1
