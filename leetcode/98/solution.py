class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0
        n = len(s)
        dp = [1] * n
        for i in range(1, n):
            if s[i] == '0' and s[i-1] not in ['1','2']:
                return 0
            if s[i] == '0':
                dp[i] = dp[i-2]
            elif 10 < int(s[i-1]+s[i]) <= 26:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[n-1]


print(Solution().numDecodings("10011"))
print(Solution().numDecodings("2101"))
print(Solution().numDecodings("109"))
print(Solution().numDecodings("119"))
