matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
rows, cols = len(matrix), len(matrix[0])
for i in range(rows):
     if i % 2 == 0:
        for j in range(cols):
             print(matrix[i][j], end=' ')
     else:
        for j in range(cols - 1, -1, -1):
         print(matrix[i][j], end=' ')