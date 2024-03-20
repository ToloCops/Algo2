def DFSr(u: int, G: list[list[int]], V: list[int], S: list[int]):
    V[u] = 1
    for v in G[u]:
        if V[v] == 0:
            DFSr(v, G, V, S)
    S.append(u)

def find_sequence(G: list[list[int]]) -> list[int]:
    u = 0
    V = [0] * len(G)
    S: list[int] = []
    DFSr(u, G, V, S)
    return S

G = [[3, 4, 5, 8], [2, 7], [1, 6, 7], [0, 4, 7], [0, 3], [0, 8], [2], [1, 2, 3], [0, 5]]
print(find_sequence(G))