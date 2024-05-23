def es(s: str, I: set):
    T = [0] * len(s)
    if s[0] in I:
        T[0] = 1
    for i in range(1, len(s)):
        if s[i] in I:
            T[i] += T[i - 1]
        if s[i - 1 : i + 1] in I:
            if i == 1:
                T[i] += 1
            else:
                T[i] += T[i - 2]
    return T


print(es("0011010", {"0", "01", "10"}))
