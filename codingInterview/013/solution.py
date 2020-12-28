import sys
sys.setrecursionlimit(10000)


class Solution:
    @staticmethod
    def solve():
        useable = [[0] * n for _ in range(m)]
        Solution.bfs(0, 0, useable)
        return sum(sum(k) for k in useable)

    @staticmethod
    def bfs(i, j, useable):
        if Solution.total(i, 0) + Solution.total(j, 0) > k:
            return False
        useable[i][j] = 1
        for pos in direction:
            i += pos[0]
            j += pos[1]
            if 0 <= i < m and 0 <= j < n and useable[i][j] == 0:
                Solution.bfs(i, j, useable)
            i -= pos[0]
            j -= pos[1]
        return False

    @staticmethod
    def total(m, sum):
        if m == 0:
            return sum
        return Solution.total(m//10, m % 10+sum)


direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]
k = 18
m = 40
n = 40
print(Solution.solve())
