from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        for i in range(1,n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        dp2 = [0] * n
        for i in range(0, n-1):
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i])
        return max(dp[n-1], dp2[n-2])


print(Solution().rob([1]))
# print(Solution().rob([2,3,2]))
# print(Solution().rob([1,2,3,1]))
# print(Solution().rob([0]))
