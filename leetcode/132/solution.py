class Solution:
    def minCut(self, s: str) -> int:
        return self.dfs(s)

    def dfs(self, s: str) -> int:
        if self.is_round(s):
            return 0
        n = len(s)
        ans = 2000
        for i in range(n-1):
            re = self.dfs(s[0:i+1]) + 1 + self.dfs(s[i+1:])
            if re < ans:
                ans = re
        return ans

    def is_round(self, s: str) -> bool:
        n = len(s)
        l = 0
        r = n-1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


# TODO dp
# print(Solution().minCut("aab"))
# print(Solution().minCut("aba"))
print(Solution().minCut("eegiicgaeadbcfacfh"))
