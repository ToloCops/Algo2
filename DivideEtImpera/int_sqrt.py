# Errata


def int_sqrt(n: int, i: int) -> int:
    i = i // 2
    if i * i <= n and i * (i + 1) > n:
        return i
    else:
        return int_sqrt(n, i)


n = 36
print(int_sqrt(n, n))
