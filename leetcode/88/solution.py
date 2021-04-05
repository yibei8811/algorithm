from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p = 0
        q = 0
        for index in reversed(range(len(nums1))):
            if index >= m:
                nums1.pop(index)
        while q < n:
            while p < m and nums2[q] > nums1[p]:
                p += 1
            nums1.insert(p, nums2[q])
            m += 1
            q += 1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
Solution().merge(nums1,3,nums2,3)
print(nums1)
