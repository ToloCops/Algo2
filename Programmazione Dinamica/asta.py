def es(V: list[int]) -> int:
    T = [0] * len(V)
    for i in range(1, len(V)):
        max_profit = V[i]
        for k in range(i):
            max_profit = max(max_profit, V[k] + T[i - k])
        T[i] = max_profit
    return T[-1]


print(es([0, 1, 5, 8, 9, 10, 17, 17, 20]))
