def count_sink_from(u: int, G: list[list[int]], V: list[int]) -> int:
    V[u] = 1
    if G[u] == []: return 1
    count = 0
    for x in G[u]:
        if V[x] == 0:
            count += conta_pozzi_da(x, G, V)
    return count

G: list[list[int]] = [
    [9, 2],
    [0, 2, 5, 7],
    [],
    [4, 6],
    [10],
    [],
    [9],
    [8],
    [],
    [10],
    [3]
]

u = 1
V = [0] * len(G)
print(count_sink_from(u, G, V))