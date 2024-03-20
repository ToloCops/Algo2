def path_to_root(P: list[int], u: int) -> list[int]:
    path = []
    path.append(u)
    while P[u] != u:
        path.append(P[u])
        u = P[u]
    return path

def distance1(P: list[int], u: int, v: int) -> int:
    path_u = path_to_root(P, u)
    path_v = path_to_root(P, v)

    count_fathers = [0] * len(P)
    common_father = 0
    for u, v in zip(path_u, path_v):
        count_fathers[u] += 1
        count_fathers[v] += 1
        if count_fathers[u] == 2:
            common_father = u
            break
        elif count_fathers[v] == 2: 
            common_father = v
            break
    
    count_u = 0
    for u in path_u:
        if u == common_father: break
        count_u += 1
    
    count_v = 0
    for v in path_v:
        if v == common_father: break
        count_v += 1
    
    return count_u + count_v


P = [1, 1, 0, 1, 3, 2, 2, 8, 0]
u = 8
v = 3

print(distance1(P, u, v))