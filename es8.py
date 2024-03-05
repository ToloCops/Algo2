def complete_graph_gen(n: int) -> list[list[int]]:
    """
    Generates a complete graph with 'n' nodes.

    Args:
        n (int): The number of nodes in the graph.

    Returns:
        list[list[int]]: The adjacency list representation of the complete graph.

    """
    G: list[list[int]] = [[] for _ in range(n)]
    for x in range(n):
        for i in range(n):
            if i != x: G[x].append(i)
    return G

def edge_orienting(u: int, G: list[list[int]], V: list[int]) -> list[list[int]]:
    """
    Orient the edges of a graph such that there are no cycles.

    Args:
        u (int): The current vertex.
        G (list[list[int]]): The adjacency list representation of the graph.
        V (list[int]): The visited array.

    Returns:
        list[list[int]]: The updated adjacency list representation of the graph.

    """
    V[u] = 1
    for x in reversed(G[u]):
        if V[x] == 0:
            G[x].pop()
    if u == 0: return G
    return edge_orienting(u-1, G, V)

def orient_all(u: int, G: list[list[int]], V: list[int]) -> list[list[int]]:
    """
    Recursively orients all not oriented edges in the graph G such that there are no cycles

    Args:
        u (int): The starting vertex.
        G (list[list[int]]): The adjacency list representation of the graph.
        V (list[int]): A list to keep track of visited vertices.

    Returns:
        list[list[int]]: The updated adjacency list representation of the graph with oriented edges.
    """
    V[u] = 1
    for x in G[u]:
        if V[x] == 0:
            if u in G[x]: 
                G[u].remove(x)
                orient_all(x, G, V)
            else: 
                orient_all(x, G, V)
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