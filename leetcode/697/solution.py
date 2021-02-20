from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dict = {}
        max = 0
        for i in range(n):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1
            if dict[nums[i]] > max:
                max = dict[nums[i]]
        result = n
        for i in dict:
            if dict[i] == max:
                l = 0
                while nums[l] != i:
                    l += 1
                r = n-1
                while nums[r] != i:
                    r -= 1
                if r-l+1 < result:
                    result = r-l+1
        return result


print(Solution().findShortestSubArray([1, 2, 2, 3, 1]))
print(Solution().findShortestSubArray([1,2,2,3,1,4,2]))

