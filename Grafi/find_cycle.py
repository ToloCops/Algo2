def DFSr_undirected(u: int, father: int, G: list[list[int]], V: list[int]) -> bool:
    V[u] = 1
    for v in G[u]:
        if V[u] == 1:
            if v != father: return True
        else:
            if DFSr_undirected(v, u, G, V): return True
    return False 

def DFSr_directed(u: int, G: list[list[int]], V: list[int]) -> bool:
    V[u] = 1
    for v in G[u]:
        if V[u] == 1: return True
        if V[u] == 0:
            if DFSr_directed(v, G, V): return True
    V[u] = 2
    return False

def cycle(u: int, G: list[list[int]], directed: bool = False) -> bool:
    V = [0] * len(G)
    if directed: return DFSr_directed(u, G, V)
    return DFSr_undirected(u, u, G, V)
