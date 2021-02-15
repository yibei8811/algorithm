from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        count = 0
        for i in range(0, n):
            if nums[i] == 1:
                dp[i] = count + 1 if (count + 1) > dp[i-1] else dp[i-1]
                count += 1
            else:
                count = 0
                dp[i] = dp[i-1]
        return dp[n-1]


Solution().findMaxConsecutiveOnes([1,1,0,1,1,1])
