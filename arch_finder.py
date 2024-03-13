def DFSr_directed(u: int, G: list[list[int]], V: list[int]) -> bool:
    V[u] = 1
    for v in G[u]:
        if V[u] == 1: return True
        if V[u] == 0:
            if DFSr_directed(v, G, V): return True
    V[u] = 2
    return False


def find_archs(G: list[list[int]]) -> tuple[int, int, int]:
    
    return 0, 0, 0



G = [[1, 2], [3], [3], [4, 5], [5], [6], [1]]
print(find_archs(G))