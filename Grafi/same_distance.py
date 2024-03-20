def BFS_d(u: int, G: list[list[int]]) -> list[int]:
    D = [-1] * len(G)
    D[u] = 0
    coda = [u]
    i = 0
    while len(coda) > i:
        x = coda[i]
        i += 1
        for y in G[x]:
            if D[y] == -1:
                D[y] = D[x] + 1
                coda.append(y)
    return D


def same_distance(u:int, v:int, G:list[list[int]]) -> list[int]:
    D_u = BFS_d(u, G)
    D_v = BFS_d(v, G)
    same_distance = []
    for i in range(len(G)):
        if D_u[i] == D_v[i]: same_distance.append(i)
    return same_distance
G: list[list[int]]=[ [1,5], [2], [3], [4], [ ], [2,4], [2] ]
u = 6
v = 5
print(same_distance(u, v, G))