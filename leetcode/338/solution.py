from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            if i & 1 == 1:
                dp[i] = dp[i-1] + 1
            else:
                j = 1
                while i & (1 << j) == 0:
                    j += 1
                dp[i] = dp[i-1] + 1 - j
        return dp


print(Solution().countBits(2))
print(Solution().countBits(5))
