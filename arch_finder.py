def DFSr(u: int, G: list[list[int]], V: list[int], D: list[int], archs: list[int], time: list[int] = [0]):
    V[u] = 1
    D[u] = time[0]
    time[0] += 1
    for v in G[u]:
        if V[v] == 1: archs[1] += 1
        elif V[v] == 0:
            DFSr(v, G, V, D, archs, time)
        elif V[v] == 2:
            if D[u] < D[v] : archs[0] += 1
            else: archs[2] += 1
    V[u] = 2


def find_archs(G: list[list[int]]) -> list[int]:
    archs = [0, 0, 0]
    V = [0] * len(G)
    D = [0] * len(G) #lista contenente il momento in cui i nodi sono stati scoperti
    DFSr(0, G, V, D, archs)
    return archs



G = [[1, 2], [3], [3], [4, 5], [5], [6], [1]]
print(find_archs(G))