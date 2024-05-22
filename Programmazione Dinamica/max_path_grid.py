def es(M: list[list[int]]) -> int:
    n = len(M)
    T = [[0] * n for _ in range(n)]
    k = 1
    max_length = 0
    for i in range(n):
        for j in range(n):
            if T[i][j] != 0:
                continue
            else:
                l = [0]
                mark_neighbours(M, T, i, j, k, n, l)
                k += 1
                max_length = max(max_length, l[0])
    return max_length


def mark_neighbours(M, T, i, j, k, n, l):
    if T[i][j] != 0:
        return
    T[i][j] = k
    l[0] += 1
    if i != 0:
        # checking up
        if abs(M[i - 1][j] - M[i][j]) == 1:
            mark_neighbours(M, T, i - 1, j, k, n, l)
    if j != 0:
        # checking left
        if abs(M[i][j - 1] - M[i][j]) == 1:
            mark_neighbours(M, T, i, j - 1, k, n, l)
    if j != n - 1:
        # cheking right
        if abs(M[i][j + 1] - M[i][j]) == 1:
            mark_neighbours(M, T, i, j + 1, k, n, l)
    if i != n - 1:
        # checking down
        if abs(M[i + 1][j] - M[i][j]) == 1:
            mark_neighbours(M, T, i + 1, j, k, n, l)


M = [[9, 7, 6], [8, 2, 5], [1, 3, 4]]

print(es(M))
