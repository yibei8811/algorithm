from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(nums)
        m = len(nums[0])
        next = self.next(nums, n, m)
        if n * m < r * c:
            return nums
        ret = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                ret[i][j] = next()
        return ret

    def next(self, nums, n, m):
        k = 0
        l = -1
        def call():
            nonlocal k
            nonlocal l
            if l < m-1:
                l += 1
            else:
                k += 1
                l = 0
            return nums[k][l]
        return call


print(Solution().matrixReshape([[1,2],[3,4]], 1, 4))
