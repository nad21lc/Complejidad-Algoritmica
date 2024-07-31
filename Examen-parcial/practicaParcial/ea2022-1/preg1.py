# Pregunta 1
# (4 puntos)
# Implemente una variación del algoritmo DFS, al que llamaremos RDFS, en el que se deberán acceder
# a los vecinos de cada nodo de manera aleatoria. Por ejemplo dado el grafo siguiente en lista de
# adyacencia:
# 0: 1, 5
# 1: 0, 2, 3
# 2: 1, 3, 4
# 3: 1, 2, 5
# 4: 2, 5
# 5: 0, 3, 4
# El DFS tradicional iniciado desde el nodo cero siempre recorrerá primero al 1 y luego al 5, desde el 1,
# intentará ir al 0 (que ya está visitado) luego al 2 y luego al 3 y así sucesivamente.
# Lo que se le pide es que si ejecutamos el algoritmo solicitado RDFS, partiendo del nodo 0, podría ir
# primero al nodo 5 antes que al 1, y en otra ocasión podría ir al 1 y luego al 5, etc.
# Elabore 3 grafos distintos y realice varias ejecuciones donde se debe mostrar que los resultados son
# distintos cada vez.

import graphviz as gv
import random

def rdfs(graph, node, visited):
    visited[node] = True
    print(node)  # Puedes hacer lo que necesites con el nodo, como imprimirlo
    neighbors = graph[node]
    random.shuffle(neighbors)  # Mezclar aleatoriamente los vecinos
    for neighbor in neighbors:
        if not visited[neighbor]:
            rdfs(graph, neighbor, visited)

# Ejemplo de uso con un grafo representado como un diccionario de listas de adyacencia
graph = {
    0: [1, 5],
    1: [0, 2, 3],
    2: [1, 3, 4],
    3: [1, 2, 5],
    4: [2, 5],
    5: [0, 3, 4]
}

visited = [False] * len(graph)

# Llamada inicial a RDFS desde el nodo 0
rdfs(graph, 0, visited)