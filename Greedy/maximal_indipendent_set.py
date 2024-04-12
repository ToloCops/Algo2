## Given an acyclic non directed graph, returns the maximal indipendent set of
## nodes in it

def find_a_big_root(G: list[list[int]]) -> int:
    """
    Finds the root with the max number of sons in the graph.

    Args:
        G (list[list[int]]): The adjacency list representation of the graph.

    Returns:
        int: The index of the big root in the graph.
    """
    root = 0
    sons = len(G[0])
    for i in range(len(G)):
        if len(G[i]) > sons:
            root = i
            sons = len(G[i])
    return root

def DFS_m(G: list[list[int]], u: int, ind_set: list[int], V: list[int]):
    """
    Performs a depth-first search (DFS) traversal on a graph to find a maximal independent set.

    Args:
        G (list[list[int]]): The adjacency list representation of the graph.
        u (int): The current vertex being visited.
        ind_set (list[int]): The list to store the vertices in the maximal independent set.
        V (list[int]): The list to keep track of visited vertices.

    Returns:
        None
    """
    V[u] = 1
    sons = len(G[u])
    for x in G[u]:
        if V[x] == 0:
            if len(G[x]) < sons:
                ind_set.append(x)
            DFS_m(G, x, ind_set, V)


def max_ind_set(G: list[list[int]]) -> list[int]:
    """
    Finds a maximal independent set in a given graph.

    Parameters:
    G (list[list[int]]): The adjacency matrix representation of the graph.

    Returns:
    list[int]: The list of vertices in the maximal independent set.
    """
    r = find_a_big_root(G)
    ind_set: list[int] = []
    V = [0] * len(G)
    DFS_m(G, r, ind_set, V, )
    return ind_set

G: list[list[int]] = [[4], [2], [8, 1, 4], [5], [0, 2, 9], [3, 6, 7, 8], [5], [5], [2, 5], [4]]

print(max_ind_set(G))