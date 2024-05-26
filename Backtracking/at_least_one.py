def es(n: int, i: int, S: list[int], k: int, counts: list[int], rimanenti: int, c):
    if i < n:
        for j in range(k):
            if counts[j] > 0:
                if n - i - 1 >= rimanenti:
                    S.append(j)
                    es(n, i + 1, S, k, counts, rimanenti, c)
                    S.pop()
            else:
                counts[j] = 1
                S.append(j)
                es(n, i + 1, S, k, counts, rimanenti - 1, c)
                counts[j] = 0
                S.pop()
    else:
        c[0] += 1
        print(c[0], S)


es(4, 0, [], 3, [0] * 3, 3, [0])
