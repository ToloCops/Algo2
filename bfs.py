def BFS(x: int, G: list[list[int]]) -> list[int]:
    V = [0] * len(G)
    V[x] = 1
    coda = [x]
    i = 0
    while len(coda) > i:
        u = coda[i]
        i += 1
        for y in G[u]:
            if V[y] == 0:
                V[y] = 1
                coda.append(y)
    return V

def BFSpadri(x: int, G: list[list[int]]) -> list[int]:
    P = [-1] * len(G)
    P[x] = x
    coda = [x] 
    i = 0
    while len(coda) > i:
        u = coda[i]
        i += 1
        for y in G[u]:
            if P[y] == -1:
                P[y] = u
                coda.append(y)
    return P

def BFSdistanze(x: int, G: list[list[int]]) -> list[int]:
    D = [-1] * len(G)
    D[x] = 0
    coda = [x]
    i = 0
    while len(coda) > i:
        u = coda[i]
        i += 1
        for y in G[u]:
            if D[y] == -1:
                D[y] = D[u] + 1
                coda.append(y)
    return D