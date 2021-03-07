from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        ret = []
        self.dfs(s, res, ret)
        return ret

    def dfs(self, s: str, res, ret) -> List[List[str]]:
        if len(s) == 0:
            ret.append(res[::])
            return
        n = len(s)
        for i in range(1, n+1):
            if self.is_round(s[0:i]):
                res.append(s[0:i])
                self.dfs(s[i:], res, ret)
                res.pop(-1)

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


print(Solution().partition("aab"))
# TODO dp预处理的思路很好
