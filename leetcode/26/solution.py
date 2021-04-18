from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        for i in reversed(range(n-1)):
            if nums[i] == nums[i+1]:
                # nums.remove(nums[i])
                del nums[i]
        return len(nums)


# del nums[i] 和 nums.remove(nums[i]) 速度相差很大
# 根据下标 和 搜索元素的区别

