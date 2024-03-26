def crea(G: list[list[int]]) -> list[tuple[int, int]]:
    C = [(i, 1) for i in range(len(G))]
    return C

def find(u: int, C: list[tuple[int, int]]) -> int:
    while u != C[u][0]:
        u = C[u][0]
    return u

def union(a: int, b: int, C: list[tuple[int, int]]):
    tot_a, tot_b = C[a][1], C[b][1]
    if tot_a >= tot_b:
        C[a] = (a, tot_a + tot_b)
        C[b] = (a, tot_b)
    else:
        C[b] = (b, tot_a + tot_b)
        C[a] = (b, tot_a)