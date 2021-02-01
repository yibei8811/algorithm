import random


class Solution:
    @staticmethod
    def dfs(n, s, res):
        if len(n) == 0:
            return res.append(s)
        Solution.dfs(n[1:], s + ',' + n[0], res)
        if len(n) > 1 and 10 <= int(n[0:2]) < 26:
            Solution.dfs(n[2:], s + ',' + n[0:2], res)
        return res

    @staticmethod
    def solve1(n):
        return len(Solution.dfs(n, '', []))

    @staticmethod
    def solve2(n):
        l = len(n)
        dp = [0] * (l+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, l+1):
            if 10 <= int(n[i-2:i]) < 26:
                dp[i] = dp[i-1]+dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[l]


for i in range(0,100):
    random.seed(i)
    s = str(random.randrange(1,99999999))
    r1 = Solution.solve1(s)
    r2 = Solution.solve2(s)
    if Solution.solve1(s) == Solution.solve2(s):
        pass
    else:
        print(s)
        print(r1)
        print(r2)
