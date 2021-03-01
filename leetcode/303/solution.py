from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.nums = nums
        sums = [0] * n
        for i in range(n):
            sums[i] = nums[i] + sums[i-1]
        self.sums = sums

    def sumRange(self, i: int, j: int) -> int:
        n = len(self.nums)
        if 0 > i >= n or 0 > j >= n:
            return None
        return self.sums[j] - self.sums[i] + self.nums[i]


numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2))
print(numArray.sumRange(2, 5))
print(numArray.sumRange(0, 5))
