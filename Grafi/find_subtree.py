def path_to_root(P: list[int], u: int, x: int) -> tuple[list[int], bool]:
    path = []
    is_sub = False
    path.append(u)
    if u == x: 
        is_sub = True
        return path, is_sub
    while P[u] != u:
        if P[u] == -1: 
            break
        elif P[u] == -2:
            is_sub = True
            break
        path.append(P[u])
        u = P[u]
        if u == x: 
            is_sub = True
            break
    return path, is_sub

def subtree(P: list[int], x: int) -> list[int]:
    subtree = []
    for i in range(len(P)):
        if P[i] != -1:
            path, is_sub = path_to_root(P, i, x)
            if not is_sub:
                for u in path:
                    P[u] = -1
            else:
                for u in path:
                    P[u] = -2
    for i in range(len(P)):
        if P[i] != -1: subtree.append(i+1)
    return subtree

P = [2, 3, 2, 4, 2, 3, 4, 0]
x = 4

print(subtree(P, x))