from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                ans[j][i] = matrix[i][j]
        return ans


print(Solution().transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().transpose([[1,2,3],[4,5,6]]))
