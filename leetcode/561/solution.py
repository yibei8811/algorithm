from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        r = 0
        for i in range(0, n, 2):
           r += nums[i]
        return r


# 和最大即为损失最小，排序后，每2给相邻的损失最小，是总和也是损失最小的
nums = [6,2,6,5,1,2]
print(Solution().arrayPairSum(nums))