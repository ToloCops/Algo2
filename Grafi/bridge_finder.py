from math import inf

def DFSr(x: int, h: int, G: list[list[int]], Height: list[int], P: list[tuple]) -> float:
    Height[x] = h
    ret = inf
    for y in G[x]:
        if Height[y] == -1:
            a = DFSr(y, h+1, G, Height, P)
            if h < a:
                P.append((x, y))
            ret = min(ret, a)
        elif Height[y] != h-1:
            ret = min(ret, Height[y])
    return ret

def find_bridges(G: list[list[int]]) -> list[tuple]:
    Height = [-1] * len(G)
    P: list[tuple] = []
    DFSr(0, 0, G, Height, P)
    return P

G = [[3, 4, 5, 8], [2, 7], [1, 6, 7], [0, 4, 7], [0, 3], [0, 8], [2], [1, 2, 3], [0, 5]]
print(find_bridges(G))