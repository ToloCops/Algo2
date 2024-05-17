def cerca_percorso(n):
    scacchiera = [[0 for _ in range(n)] for _ in range(n)]
    gameState = [[0 for _ in range(n)] for _ in range(n)]
    for y, riga in enumerate(gameState):
        for x, cella in enumerate(riga):
            if x + 2 < n and y + 1 < n:
                gameState[y + 1][x + 2] += 1
            if x + 2 < n and y - 1 >= 0:
                gameState[y - 1][x + 2] += 1
            if x - 2 >= 0 and y + 1 < n:
                gameState[y + 1][x - 2] += 1
            if x - 2 >= 0 and y - 1 >= 0:
                gameState[y - 1][x - 2] += 1

            if x + 1 < n and y + 2 < n:
                gameState[y + 2][x + 1] += 1
            if x + 1 < n and y - 2 >= 0:
                gameState[y - 2][x + 1] += 1
            if x - 1 >= 0 and y + 2 < n:
                gameState[y + 2][x - 1] += 1
            if x - 1 >= 0 and y - 2 >= 0:
                gameState[y - 2][x - 1] += 1
    backtracking(gameState, 0, 0)
    return

def backtracking(gameState: list[list[int]], i: int, j: int):
    for cell in availableMoves(gameState, i, j):
        


if __name__ == "__main__":
    cerca_percorso(4)
