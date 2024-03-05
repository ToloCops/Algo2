def complete_graph_gen(n: int) -> list[list[int]]:
    G: list[list[int]] = [[] for _ in range(n)]
    for x in range(n):
        for i in range(n):
            if i != x: G[x].append(i)
    return G

G = complete_graph_gen(3)