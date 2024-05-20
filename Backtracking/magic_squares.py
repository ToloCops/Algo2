def is_magic(square, n, magic_sum):
    # Controlla le righe
    for row in range(n):
        if sum(square[row]) != magic_sum:
            return False

    # Controlla le colonne
    for col in range(n):
        if sum(square[row][col] for row in range(n)) != magic_sum:
            return False

    # Controlla la diagonale principale
    if sum(square[i][i] for i in range(n)) != magic_sum:
        return False

    # Controlla la diagonale secondaria
    if sum(square[i][n - 1 - i] for i in range(n)) != magic_sum:
        return False

    return True


def solve_magic_square(n):
    def backtrack(pos):
        if pos == n * n:
            if is_magic(square, n, magic_sum):
                magic_squares.append([row[:] for row in square])
            return

        row, col = divmod(pos, n)
        for num in range(1, n * n + 1):
            if num not in used:
                square[row][col] = num
                used.add(num)
                backtrack(pos + 1)
                used.remove(num)
                square[row][col] = 0

    magic_sum = n * (n * n + 1) // 2
    square = [[0] * n for _ in range(n)]
    used = set()
    magic_squares = []

    backtrack(0)
    return magic_squares


# Esempio di utilizzo
n = 4
magic_squares = solve_magic_square(n)
print(f"Numero di quadrati magici di ordine {n}: {len(magic_squares)}")
for square in magic_squares:
    for row in square:
        print(row)
    print()
