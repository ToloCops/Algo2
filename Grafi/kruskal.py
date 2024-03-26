from union_find import *

def kruskal(G: list[list[tuple[int, int]]]) -> list[list[int]]:
    E: list[tuple[int, int, int]] = [(c, u, v) for u in range(len(G)) for v, c in G[u] if u < v]
    E.sort(reverse=True)
    T: list[list[int]] = [[] for _ in G]
    C = crea(T)
    while E:
        c,x,y = E.pop()
        cx = find(x, C)
        cy = find(y, C)
        if cx != cy:
            T[x].append(y)
            T[y].append(x)
            union(cx, cy, C)
    return T