"""
Un problema clásico para sobreponer imágenes es la eliminación de las líneas ocultas. 
En el caso en 2D el objetivo es de dibujar el skyline de una ciudad. 
Para simplificar, supongamos que todos los edificios corresponden (por proyección) a rectángulos 
que comparten toda la misma base (i.e. la ciudad es plana). 
Un edificio es una tripleta (g, h, d), d > g ≥ 0, h ≥ 0 
que representa al rectángulo (g, 0), (g, h), (d, h), (d, 0). 
Por ejemplo, para 6 edificios dados por 
(3, 13, 9), (1, 11, 5), (19, 18, 22), (3, 6, 7), (16, 3, 25), (12, 7, 16) (ver la figura 1a), 
el skyline obtenido será dado por la figura 1b.
"""

import heapq

def getSkyline(edificios):
    if not edificios:
        return []
    critical_points = []
    for g, h, d in edificios:
        critical_points.append((g, -h, d))
        critical_points.append((d, 0, None))

    critical_points.sort(key=lambda x: (x[0], x[1]))

    skyline = []

    heights = [(0, float('inf'))] 

    for x, h, d in critical_points:
        while heights[0][1] <= x:
            heapq.heappop(heights)

        if h != 0:
            heapq.heappush(heights, (h, d))

        current_max_height = -heights[0][0]

        if not skyline or current_max_height != skyline[-1][1]:
            skyline.append((x, current_max_height))

    return skyline


edificios = [(3, 13, 9), (1, 11, 5), (19, 18, 22), (3, 6, 7), (16, 3, 25), (12, 7, 16)]
result = getSkyline(edificios)
print(result)
