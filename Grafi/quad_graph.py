def quad(G: list[list[int]]) -> list[list[int]]:
    u = 0
    Q: list[list[int]] = [[] for _ in range(len(G))]
    print(Q)
    V = [0] * len(G)
    quad_1(u, G, Q, V)
    return Q
        
def quad_1(u: int, G: list[list[int]], Q: list[list[int]], V: list[int]):
    V[u] = 1
    for i in G[u]:
        Q[u].append(i)
        if G[i] != []:
            for x in G[i]:
                Q[u].append(x)
        if V[i] == 0: quad_1(i, G, Q, V)
        

G: list[list[int]] = [
    [1],
    [2], 
    [3],
    [4],
    [5],
    [0]
]

print(quad(G))
