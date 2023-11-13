def is_safe(board, row, col, n):
    # Check if there is a queen in the same row
    if any(board[row]):
        return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower-left diagonal
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col, n):
    if col == n:
        # All queens are placed successfully
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solve_nqueens(board, col + 1, n):
                return True

            # If placing a queen in the current position doesn't lead to a solution, backtrack
            board[i][col] = 0

    # If no place is found in this column, backtrack
    return False

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def solve_nqueens_main(n):
    board = [[0] * n for _ in range(n)]

    if not solve_nqueens(board, 0, n):
        print("Solution does not exist.")
    else:
        print_board(board)

# Example usage:
n = 4  # Change this to the desired number of queens
solve_nqueens_main(n)
