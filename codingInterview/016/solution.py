class Solution:
    @staticmethod
    def solve(base, ex):
        dp = [0] * (ex + 1)
        dp[0] = 1
        dp[1] = base
        for i in range(2,ex+1):
            dp[i] = dp[i//2] * dp[i//2]
            if i % 2 == 1:
                dp[i] = dp[i] * base
        return dp[ex]


print(Solution.solve(2,10))
print(Solution.solve(2,11))
print(Solution.solve(2,12))
print(Solution.solve(3,3))
print(Solution.solve(3,4))
print(Solution.solve(3,5))
