def fill_spiral_matrix(n):
    matrix = [[' ' for _ in range(n)] for _ in range(n)]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    direction_index = 0
    row, col = 0, 0

    for char in range(ord('A'), ord('Z') + 1):
        matrix[row][col] = chr(char)
        next_row, next_col = row + directions[direction_index][0], col + directions[direction_index][1]

        if (
            0 <= next_row < n
            and 0 <= next_col < n
            and matrix[next_row][next_col] == ' '
        ):
            row, col = next_row, next_col
        else:
            direction_index = (direction_index + 1) % 4
            row, col = row + directions[direction_index][0], col + directions[direction_index][1]

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))


if __name__ == "__main__":
    n = 5  # You can change this to the desired size of the matrix
    spiral_matrix = fill_spiral_matrix(n)
    print_matrix(spiral_matrix)
