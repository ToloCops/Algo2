def es(n: int, i: int, s: str, j, k, found):
    if j == k:
        found = True
    if i < n:
        s += "0"
        es(n, i + 1, s, j + 1, k, found)
        s = s[:-1]
        if n - i > k or found:
            s += "1"
            j = 0
            es(n, i + 1, s, j, k, found)
    else:
        print(s)


es(4, 0, "", 0, 2, False)
