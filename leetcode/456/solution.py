from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        max_3 = None
        queue = [nums[n-1]]
        for i in range(n-2, -1, -1):
            if max_3 is not None and nums[i] < max_3:
                return True
            while len(queue) > 0 and nums[i] > queue[-1]:
                max_3 = queue.pop(-1)
            if nums[i] != max_3:
                queue.append(nums[i])
        return False


# TODO better
print(Solution().find132pattern([1,2,3,4]))
print(Solution().find132pattern([3,1,4,2]))
print(Solution().find132pattern([-1,3,2,0]))
