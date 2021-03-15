from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix[0])
        n = len(matrix)
        ans = []
        vis = [[0] * m for _ in range(n)]
        i = 0
        j = 0
        while True:
            while j < m and vis[i][j] == 0:
                ans.append(matrix[i][j])
                vis[i][j] = 1
                j += 1
            j -= 1
            i += 1
            if i >= n or vis[i][j] == 1:
                break
            while i < n and vis[i][j] == 0:
                ans.append(matrix[i][j])
                vis[i][j] = 1
                i += 1
            i -= 1
            j -= 1
            if vis[i][j] == 1:
                break
            while j >= 0 and vis[i][j] == 0:
                ans.append(matrix[i][j])
                vis[i][j] = 1
                j -= 1
            j += 1
            i -= 1
            if vis[i][j] == 1:
                break
            while i >= 0 and vis[i][j] == 0:
                ans.append(matrix[i][j])
                vis[i][j] = 1
                i -= 1
            i += 1
            j += 1
            if vis[i][j] == 1:
                break
        return ans


print(Solution().spiralOrder([[1]]))
print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
