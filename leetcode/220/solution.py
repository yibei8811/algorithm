from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        w = t + 1
        dict = {}
        for i in range(n):
            id = nums[i] // w
            if id in dict:
                return True
            if id + 1 in dict and -t <= dict[id+1] - nums[i] <= t:
                return True
            if id - 1 in dict and -t <= dict[id-1] - nums[i] <= t:
                return True
            dict[id] = nums[i]
            if i >= k:
                dict.pop(nums[i-k]//w)
        return False


# print(Solution().containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))
# print(Solution().containsNearbyAlmostDuplicate([1,0,1,1], 1, 2))
# print(Solution().containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))
print(Solution().containsNearbyAlmostDuplicate([-3,3,-6],2,3))
