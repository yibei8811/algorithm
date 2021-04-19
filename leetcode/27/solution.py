from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        p = 0
        q = n-1
        while p <= q:
            while p <= q and  p < n and nums[p] != val:
                p += 1
            while p <= q and q >= 0 and nums[q] == val:
                q -= 1
            if p < q:
                nums[p] = nums[p] ^ nums[q]
                nums[q] = nums[p] ^ nums[q]
                nums[p] = nums[p] ^ nums[q]
        return p


num = [3,2,2,3]
print(Solution().removeElement(num,3))
print(num)
