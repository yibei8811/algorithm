from typing import List


class Solution:
    # 无重复 todo test
    # def combinationSum4(self, nums: List[int], target: int) -> int:
    #     n = len(nums)
    #     dp = [[0] * (target+1) for _ in range(n)]
    #     for i in range(n):
    #         for j in range(1, target+1):
    #             dp[i][j] += dp[i - 1][j]
    #             if nums[i] == j:
    #                 dp[i][j] += 1
    #             if j - nums[i] >= 0:
    #                 dp[i][j] += dp[i - 1][j - nums[i]]
    #     return dp[n-1][target]

    # 排列
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        # ~1 dp[0] = 1  or ~2
        for i in range(target+1):
            for j in nums:
                if i == j:        # ~2
                    dp[i] += 1    # ~2
                if i-j >= 0:
                    dp[i] += dp[i-j]
        return dp[target]


# print(Solution().combinationSum4([1, 2, 3], 4))
# print(Solution().combinationSum4([9], 3))
