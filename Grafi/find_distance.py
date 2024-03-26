def BFS_d(u: int, v: int, G: list[list[int]]):
    D = [-1] * len(G)
    D[u] = 0
    coda = [u]
    i = 0
    while len(coda) > i:
        u = coda[i]
        i += 1
        for y in G[u]:
            if D[y] == -1:
                D[y] = D[u] + 1
                if y == v: return D[v]
                coda.append(y)

def distance(A: list[int], B: list[int], G: list[list[int]]) -> int:
    a_0 = len(G)
    b_0 = len(G) + 1
    G.append(A)
    G.append(B)
    for a in A:
        G[a].append(a_0)
    for b in B:
        G[b].append(b_0)
    d = BFS_d(a_0, b_0, G)
    return d-2
    

G: list[list[int]] = [
    [1, 11, 12],
    [0, 2, 10, 11],
    [1, 9, 3, 13],
    [2, 4],
    [3, 5, 8, 13],
    [4, 6, 7],
    [5, 13],
    [5, 8],
    [4, 7, 9, 10, 14],
    [2, 8, 10],
    [1, 8, 9, 14],
    [0, 1, 12],
    [0, 11],
    [2, 4, 6],
    [8, 10]
]

print(distance([5, 11, 13], [9, 14], G))