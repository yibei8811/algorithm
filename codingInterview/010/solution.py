# 0、1、1、2、3、5、8、13、21、34...
# 费氏数列...


class Solution:
    @staticmethod
    def solve(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return Solution.solve(n-1) + Solution.solve(n-2)

    @staticmethod
    def solve2(n):
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    @staticmethod
    def solve3(n, pre, now):
        if n == 1:
            return now   # 这行是return now 不是 return 1
        return Solution.solve3(n-1, now, pre+now)


for i in range(2,11):
    print(Solution.solve(i))
    print(Solution.solve2(i))
    print(Solution.solve3(i,0,1))
