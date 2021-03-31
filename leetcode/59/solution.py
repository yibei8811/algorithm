from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        num = 1
        i = 0
        j = 0
        res[i][j] = num
        while True:
            while j+1 < n and res[i][j+1] == 0:
                j += 1
                num += 1
                res[i][j] = num
            if num == n*n:
                break
            while i+1 < n and res[i+1][j] == 0:
                i += 1
                num += 1
                res[i][j] = num
            if num == n*n:
                break
            while j-1 >= 0 and res[i][j-1] == 0:
                j -= 1
                num += 1
                res[i][j] = num
            if num == n*n:
                break
            while i-1 >= 0 and res[i-1][j] == 0:
                i -= 1
                num += 1
                res[i][j] = num
            if num == n*n:
                break
        return res


print(Solution().generateMatrix(1))
