def max_unique_set(G: list[list[tuple[int, int]]]) -> tuple[list[tuple[int, int]], int]:
    """
    Finds the maximum unique set of tuples in a given graph.

    Args:
        G (list[list[tuple[int, int]]]): The input graph represented as a list of lists of tuples.
            Each tuple represents an edge in the graph, where the first element is the node index
            and the second element is the weight of the edge.

    Returns:
        list[tuple[int, int]]: The maximum unique set of tuples in the graph. A tuple is considered
            unique if its weight is the heaviest among all the tuples connected to the same node.

    """
    unique: list[tuple[int, int]] = []
    max_weight = 0
    for n in G:
        heaviest: tuple[int, int] = (-1, -1)
        for arch in n:
            if heaviest[1] < arch[1]: heaviest = arch
        if heaviest[1] > 0:
            unique.append(heaviest)
            max_weight += heaviest[1]
    return unique, max_weight

G: list[list[tuple[int, int]]] = [[(1, 2), (2, 3)],
      [(2, 1)],
      [],
      [(0, 1), (2, 4), (6, 5)],
      [(1, 2), (5, 8)],
      [(2, 8)],
      [(2, 7), (5, 3)]]  

print(max_unique_set(G))