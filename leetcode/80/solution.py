from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        num = None
        count = 0
        for i in reversed(range(n)):
            if nums[i] != num:
                num = nums[i]
                count = 0
            else:
                count += 1
                if count > 1:
                    nums.remove(nums[i])
        return len(nums)


nums = [0,0,1,1,1,1,2,3,3]
print(Solution().removeDuplicates(nums))
print(nums)
