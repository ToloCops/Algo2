def es(n: int, i: int, S: list[int], l_odds: int, r_odds: int):
    if i < n:
        for k in range(1, 4):
            S.append(k)
            if k % 2 == 1:
                es(n, i + 1, S, l_odds + 1, r_odds)
            else:
                es(n, i + 1, S, l_odds, r_odds)
            S.pop()
    elif i < 2 * n:
        for k in range(1, 4):
            if k % 2 == 1 and l_odds > r_odds:
                S.append(k)
                es(n, i + 1, S, l_odds, r_odds + 1)
                S.pop()
            elif k % 2 == 0 and (2 * n - i) > (l_odds - r_odds):
                S.append(k)
                es(n, i + 1, S, l_odds, r_odds)
                S.pop()
    else:
        print(S)


es(2, 0, [], 0, 0)
