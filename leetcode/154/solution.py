from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = n - 1
        ans = nums[0]
        while start <= end:
            mid = start + (end - start) // 2
            if nums[start] == nums[mid] == nums[end]:
                ans = min(ans, nums[start])
                start += 1
                end -= 1
            elif nums[start] <= nums[mid]:
                ans = min(ans, nums[start])
                start = mid + 1
            else:
                ans = min(ans, nums[mid])
                end = mid - 1
        return ans


print(Solution().findMin([3,1]))
