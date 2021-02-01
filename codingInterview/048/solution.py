class Solution:
    @staticmethod
    def solve(s):
        n = len(s)
        dp = [0] * n
        dp[0] = 1
        start = 0
        dict = {s[0]: 0}
        for i in range(1,n):
            index = dict.get(s[i])
            if index is None:
                dp[i] = max(dp[i-1], i - start + 1)
            else:
                if index < start:
                    dp[i] = dp[i - 1]
                else:
                    start = index + 1
                    dp[i] = max(dp[i-1], i - start + 1)
            dict[s[i]] = i
        return dp[n-1]


print(Solution.solve('arabcacfr'))
print(Solution.solve('abcadeafgh'))
