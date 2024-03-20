from math import inf

def dijkstra(s: int, G: list[list[tuple[int, int]]]) -> tuple[list[float], list[int]]:
    Inserito = [False] * len(G)
    Lista = [(inf, -1)] * len(G)
    Lista[s], Inserito[s] = (0, s), True
    for y, costo in G[s]:
        Lista[y] = (costo, s)
    while True:
        minimo = inf
        for i in range(len(Lista)):
            if not Inserito[i] and Lista[i][0] < minimo:
                minimo, x = Lista[i][0], i
        if minimo == inf: break
        Inserito[x] = True
        for y, costo in G[x]:
            if not Inserito[y] and minimo + costo < Lista[y][0]:
                Lista[y] = (minimo + costo, x)
    D = [costo for costo, _ in Lista]
    P = [padre for _, padre in Lista]
    return D, P