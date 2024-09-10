def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def solve(board, col):
        if col >= n:
            return True

        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                if solve(board, col + 1):
                    return True
                board[i][col] = 0

        return False

    board = [[0] * n for _ in range(n)]
    if solve(board, 0):
        return board
    else:
        return []

def print_board(board):
    for row in board:
        print(' '.join('Q' if col else '.' for col in row))
    print()

# Test
n = 4
board = solve_n_queens(n)
print_board(board)  # Output: Possible solution for 4-Queens Problem
