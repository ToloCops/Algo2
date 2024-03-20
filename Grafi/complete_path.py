def find_path(u: int, father: int, G: list[list[int]], path: list[int], D: list[int], time: list[int]) -> list[int]:
    path.append(u+1)
    time[0] += 1
    D[u] = time[0]
    for v in G[u]:
        if v != father:
            if D[v] == 0 or D[v] > D[u]:
                find_path(v, u, G, path, D, time)
                path.append(u+1)
    return path

G = [[1, 3, 4], [0, 2], [1, 3, 4], [0, 2, 4], [0, 2, 3]]
D = [0] * len(G)
path: list[int] = []
time = [0]

print(find_path(0, 0, G, path, D, time))
