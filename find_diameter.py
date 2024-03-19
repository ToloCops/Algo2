def max_depth_DFS(u: int, G: list[list[int]], V: list[int], max_depth: list[int], depth: int, output: list[int]) -> list[int]:
    V[u] = 1
    for x in G[u]:
        if V[x] == 0:
            max_depth_DFS(x, G, V, max_depth, depth+1, output)
    if depth > max_depth[0]:
        output[0] = u
        output[1] = depth
        max_depth[0] = depth
    return output


def find_diameterDFS(G: list[list[int]]) -> int:
    V = [0] * len(G)
    output = [0, 0]
    max_depth = [0]
    u = max_depth_DFS(0, G, V, max_depth, 0, output)[0]
    V = [0] * len(G)
    max_depth = [0]
    output = max_depth_DFS(u, G, V, max_depth, 0, output)
    return output[1]

G = [[1, 2], [0], [0, 3, 4, 5], [2, 6], [2, 7], [2, 8], [3], [4, 9], [5, 10], [7], [8]]

print(find_diameterDFS(G))