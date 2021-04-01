from typing import List


class Solution:
    # 额外M+N空间
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        flag = [0] * (n+m)
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    flag[i] = 1
                    flag[n+j] = 1
        for i in range(n+m):
            if flag[i] == 1:
                if i < n:
                    for j in range(m):
                        matrix[i][j] = 0
                else:
                    for j in range(n):
                        matrix[j][i-n] = 0


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Solution().setZeroes(matrix)
print(matrix)
