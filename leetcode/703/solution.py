# https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k - 1
        self.nums = nums
        self.nums.sort(reverse=True)
        self.r = nums[0:k]


    def add(self, val: int) -> int:
        if self.k > len(self.r) - 1:
            self.r.append(val)
            self.r.sort(reverse=True)
        else:
            if val > self.r[self.k]:
                i = 0
                while val < self.r[i]:
                    i += 1
                self.r.insert(i, val)
                self.r.pop(-1)
        return self.r[self.k]


kthLargest = KthLargest(1, [])
print(kthLargest.add(-3))
kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))
print(kthLargest.add(4))
