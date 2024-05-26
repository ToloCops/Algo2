def es(n: int, i: int, j: int, M: list[list[int]], zeros: list[int], ones: list[int]):
    if i < n:
        if j < n:
            if zeros[j] + 1 <= ones[j] or n - i >= zeros[j] + 1:
                M[i][j] = 0
                zeros[j] += 1
                es(n, i, j + 1, M, zeros, ones)
                zeros[j] -= 1
            M[i][j] = 1
            ones[j] += 1
            es(n, i, j + 1, M, zeros, ones)
            ones[j] -= 1
        else:
            es(n, i + 1, 0, M, zeros, ones)
    else:
        for row in M:
            print(row)
        print("")


M = [[0, 0], [0, 0]]

es(2, 0, 0, M, [0] * 2, [0] * 2)
