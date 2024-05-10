def es(M: list[list[int]]) -> int:
    T = [[0] * len(M[0]) for _ in range(len(M))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            if i == j == 0:
                T[i][j] = M[0][0]
            elif i == 0:
                T[0][j] = min(T[0][j - 1], M[0][j])
            elif j == 0:
                T[i][0] = T[i - 1][0] + M[i][0]
            else:
                T[i][j] = min(T[i][j - 1], T[i - 1][j] + M[i][j])
    return T[-1][-1]


if __name__ == "__main__":
    M = [[4, 5, 2], [8, 1, 9], [7, 10, 6], [4, 9, 3]]

    print(es(M))
