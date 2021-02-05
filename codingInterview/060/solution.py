import math


class Solution:
    # 排列
    # dp[n][s] = dp[n-1][s-1] ... dp[n-1][s-6]
    @staticmethod
    def solve(n, s):
        tik = [1,2,3,4,5,6]
        dp = [[0]*(s+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(1,s+1):
                for k in tik:
                    if j - k >= i - 1 >= 0:
                        dp[i][j] += dp[i-1][j-k]
        return dp[n][s]/math.pow(6, n)


# TODO 书上解答阅读
print(Solution.solve(3, 18))
print(Solution.solve(3, 3))
print(Solution.solve(3, 4))
print(Solution.solve(3, 17))
print(Solution.solve(3, 5))
print(Solution.solve(3, 16))
# tip
# 如果是组合则
# a*1+b*2+c*3+d*4+e*5+f*6 = s
# 求 dp[i][s]
# i in (1...6) 同时满足 a+ b +...+f = n
