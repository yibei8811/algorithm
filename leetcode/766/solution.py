from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        dpm = [0]*m
        dpn = [0]*n
        dpm[m-1] = 1
        dpn[n-1] = 1
        # i 即是 起点， 也是y与x的距离
        for i in range(m):
            is_eq = 1
            x = i
            y = 0
            while x + 1 < m and y + 1 < n:
                is_eq = is_eq & (matrix[x][y] == matrix[x+1][y+1])
                x += 1
                y += 1
            dpm[i] = dpm[i-1] & is_eq

        for i in range(n):
            is_eq = 1
            x = 0
            y = i
            while x + 1 < m and y + 1 < n:
                is_eq = is_eq & (matrix[x][y] == matrix[x+1][y+1])
                x += 1
                y += 1
            dpn[i] = dpn[i-1] & is_eq

        return dpm[m-1]*dpn[n-1] == 1


print(Solution().isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
print(Solution().isToeplitzMatrix( [[1,2],[2,2]]))
