import graphviz as gv

def reverseGraph(G):
    n = len(G)
    Grev = [[] for _ in range(n)]

    for u in range(n):
        for v in G[u]:
            Grev[v].append(u)
    return Grev

def dfs_first_pass(G, u, stack, visited):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            dfs_first_pass(G, v, stack, visited)
    stack.append(u)

def dfs_second_pass(G, u, component, visited):
    visited[u] = True
    component.append(u)
    for v in G[u]:
        if not visited[v]:
            dfs_second_pass(G, v, component, visited)

def kosaraju(G):
    n = len(G)
    G_rev = reverseGraph(G)

    visited = [False] * n
    stack = []
    for u in range(n):
        if not visited[u]:
            dfs_first_pass(G, u, stack, visited)

    visited = [False] * n
    components = []
    while stack:
        u = stack.pop()
        if not visited[u]:
            component = []
            dfs_second_pass(G_rev, u, component, visited)
            components.append(component)

    return components

# Grafo de las personas
G = [
    [1],
    [2, 4],
    [5],
    [1, 6],
    [3, 0],
    [7],
    [4],
    [8],
    [5],
    ]

componentesFuertementeConexos = kosaraju(G)

# Voy a nombrar a los grupos
grupos = {}
for i, componente in enumerate(componentesFuertementeConexos):
    etiqueta = f"Grupo {i+1}"
    grupos[etiqueta] = componente


def verGrafoOriginal(G):
    g = gv.Digraph()
    for u, vecinos in enumerate(G):
        for v in vecinos:
            g.edge(str(u), str(v))
    return g

grafoOriginal = verGrafoOriginal(G)
grafoOriginal.render(filename='grafo_original', format='png', cleanup=True)


def verGrafoResultante(G, grupos):
    g = gv.Digraph()
    for componente in grupos.values():
        for u in componente:
            g.node(str(u))
    for u, vecinos in enumerate(G):
        for v in vecinos:
            if u < v:
                g.edge(str(u), str(v))
    return g

grafoResultante = verGrafoResultante(G, grupos)
grafoResultante.render(filename='grafo_resultante', format='png', cleanup=True)


print("Grupos de personas en la red social:")
for etiqueta, componente in grupos.items():
    print(etiqueta, ":", componente)

# Se utilizó el algoritmo de Kosaraju para resolver el problema 
# de identificar grupos de personas estrechamente vinculados en una red social 
# representada como un grafo dirigido. Ya que Kosaraju está diseñado específicamente para 
# encontrar SCC(componentes fuertemente conexas) en un grafo dirigido.