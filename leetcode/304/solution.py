from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        if n != 0:
            m = len(matrix[0])
        for i in range(0, n):
            for j in range(0, m):
                if i-1 >= 0:
                    matrix[i][j] += matrix[i-1][j]
                if j-1 >= 0:
                    matrix[i][j] += matrix[i][j-1]
                if i-1 >= 0 and j-1 >= 0:
                    matrix[i][j] -= matrix[i-1][j-1]
        self.matrix = matrix


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = self.matrix[row2][col2]
        if row1 - 1 >= 0 and col1 - 1 >= 0:
            sum += self.matrix[row1-1][col1-1]
        if row1 - 1 >= 0:
            sum -= self.matrix[row1-1][col2]
        if col1 - 1 >= 0:
            sum -= self.matrix[row2][col1-1]
        return sum


matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
obj = NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))
