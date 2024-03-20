def DFSr(G: list[list[int]], x: int, V: list[int], sorted: list[int]):
    V[x] = 1
    for y in G[x]:
        if V[y] == 0:
            DFSr(G, y, V, sorted)
    sorted.append(x)

def topo_sort(G: list[list[int]]) -> list[int]:
    V = [0 for _ in G]
    sorted: list[int] = []
    for x in range(len(G)):
        if V[x] == 0:
            DFSr(G, x, V, sorted)
    sorted.reverse()
    return sorted

G: list[list[int]] = [[1, 4, 5], [2], [3], [4], [], [2], [2]]
print(topo_sort(G))
