class Solution:

    @staticmethod
    def solve(m, n, lst):
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = lst[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + lst[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + lst[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + lst[i][j]
        return dp[m-1][n-1]


lst = [[1,10,3,8],
       [12,2,9,6],
       [5,7,4,11],
       [3,7,16,5]]
print(Solution.solve(4, 4, lst))
