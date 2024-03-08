
def distance(P: list[int], u: int, v: int) -> int:
    
    count_u = 0
    count_v = 0
    while u != v:
        if P[u] == v:
            return count_u + 1 + count_v
        u = P[u]
        count_u += 1
        if P[v] == u:
            return count_u + 1 + count_v
        v = P[v]
        count_v += 1
    return count_u + count_v

P = [1, 1, 0, 1, 3, 2, 2, 8, 0]
u = 2
v = 5

print(distance(P, u, v))