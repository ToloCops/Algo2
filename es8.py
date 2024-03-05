def complete_graph_gen(n: int) -> list[list[int]]:
    G: list[list[int]] = [[] for _ in range(n)]
    for x in range(n):
        for i in range(n):
            if i != x: G[x].append(i)
    return G

def edge_orienting(u: int, G: list[list[int]], V: list[int]) -> list[list[int]]:
    V[u] = 1
    for x in reversed(G[u]):
        if V[x] == 0:
            G[x].pop()
    if u == 0: return G
    return edge_orienting(u-1, G, V)

def orient_all(u: int, G: list[list[int]], V: list[int]) -> list[list[int]]:
    V[u] = 1
    for x in G[u]:
        if V[x] == 0:
            if u in G[x]: 
                G[u].remove(x)
                orient_all(x, G, V)
            else: orient_all(x, G, V)
    return G

G: list[list[int]] = [
    [1],
    [3],
    [1, 4],
    [4],
    [3, 2],
    [4]
]
V = [0] * len(G)
print(G)
print(orient_all(0, G, V))