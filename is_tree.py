def es7(L: list[list[int]], V: list[int]) -> int:
    """
    Counts the number of trees in a given graph.

    Args:
        L (list[list[int]]): The adjacency list representation of the graph.
        V (list[int]): A list to keep track of visited nodes.

    Returns:
        int: The number of trees in the graph.
    """
    count = 0
    for i in range(len(L)):
        if V[i] == 0 and is_tree(i, None, L, V):
            count += 1
    return count

def is_tree(u: int, p, L: list[list[int]], V: list[int]) -> bool:
    """
    Determines whether a given graph represented by an adjacency list is a tree.

    Args:
        u (int): The current node being visited.
        p: The parent node of the current node.
        L (list[list[int]]): The adjacency list representation of the graph.
        V (list[int]): A list to keep track of visited nodes.

    Returns:
        bool: True if the graph is a tree, False otherwise.
    """
    found = True
    V[u] = 1
    for x in L[u]:
        if V[x] == 0:
            found = found and is_tree(x, u, L, V)
        elif x != p:
            return False
    return found


def DFS(u: int, L: list[list[int]], V: list[int]):
    """
    Performs a depth-first search (DFS) starting from node u in a graph represented by adjacency list L.

    Args:
        u (int): The starting node for the DFS.
        L (list[list[int]]): The adjacency list representation of the graph.
        V (list[int]): A list to keep track of visited nodes.

    Returns:
        None
    """
    V[u] = True
    for x in L[u]:
        if not V[x]:
            DFS(x, L, V)

G: list[list[int]] = [
    [1,2], # 1 -> 2,3
    [0,2], # 2 -> 1,3
    [0,1], # 3 -> 1,2
    [4,10,6], # 4 -> 5,11,7
    [3], # 5 -> 4
    [],  # 6 -> None
    [3], # 7 -> 4
    [8], # 8 -> 9
    [7], # 9 -> 8
    [10],# 10 -> 11
    [9,3], # 11 -> 10,3
    [12,13], # 12 -> 13,14
    [11,14,15], # 13 -> 12,15,16
    [11,14], # 14 -> 12,15
    [12,13], # 15 -> 13,14
    [12] # 16 -> 13
]

V = [0 for _ in range(len(G))]

if __name__ == '__main__':
    print(es7(G,V))