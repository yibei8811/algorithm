from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        left,right = 0,0
        ans = 0
        stack_min = []
        stack_max = []
        for right in range(n):
            while len(stack_min) > 0 and nums[right] < stack_min[-1]:
                stack_min.pop(-1)
            while len(stack_max) > 0 and nums[right] > stack_max[-1]:
                stack_max.pop(-1)
            stack_min.append(nums[right])
            stack_max.append(nums[right])
            if stack_max[0] - stack_min[0] > limit:
                if stack_min[0] == nums[left]:
                    stack_min.pop(0)
                if stack_max[0] == nums[left]:
                    stack_max.pop(0)
                left += 1
            else:
                ans = max(ans, right - left + 1)
        return ans


print(Solution().longestSubarray([8,2,4,7],4))
print(Solution().longestSubarray([10,1,2,4,7,2], 5))
