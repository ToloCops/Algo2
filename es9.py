def count_sink_from(u: int, G: list[list[int]], V: list[int]) -> int:
    """
    Counts the number of sink nodes reachable from a given node 'u' in a directed graph.

    Args:
        u (int): The starting node.
        G (list[list[int]]): The adjacency list representation of the directed graph.
        V (list[int]): A list to keep track of visited nodes.

    Returns:
        int: The count of sink nodes reachable from 'u'.
    """
    V[u] = 1
    if G[u] == []:
        return 1
    count = 0
    for x in G[u]:
        if V[x] == 0:
            count += count_sink_from(x, G, V)
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