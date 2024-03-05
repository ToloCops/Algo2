def complete_graph_gen(n: int) -> list[list[int]]:
    G: list[list[int]] = [[] for _ in range(n)]
    for x in range(n):
        for i in range(n):
            if i != x: G[x].append(i)
    return G

def edge_orienting(u: int, G: list[list[int]], V: list[int]) -> list[list[int]]:
    print(u)
    V[u] = 1
    for x in reversed(G[u]):
        if V[x] == 0:
            G[x].pop()
    if u == 0: return G
    else: 
        edge_orienting(u-1, G, V)
        return G


n = 4
G = complete_graph_gen(n)
V = [0] * n
print(edge_orienting(n-1, G, V))