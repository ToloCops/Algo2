def DFSr(u: int, father: int, G: list[list[int]], V: list[int], D: list[int], P: list[int], time: list[int]):
    V[u] = 1
    D[u] = time[0]
    time[0] += 1
    father_art  = True
    for x in G[u]:
        if V[x] == 0:
            DFSr(x, u, G, V, D, P, time)
        elif x != father and D[x] < D[u]:
            father_art = False
    if father_art: P.append(father)
    return

def find_points(G: list[list[int]]) -> list[int]:
    time = [0]
    V = [0] * len(G)
    D = [0] * len(G)
    P: list[int] = []
    DFSr(0, 0, G, V, D, P, time)
    return P

G = [[3, 4, 5, 8], [2, 7], [6, 7], [0, 4, 7, 8], [0, 3], [0, 8], [2], [1, 2, 3], [0, 3, 5]]

print(find_points(G))