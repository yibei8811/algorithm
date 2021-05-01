from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            sum = 0
            for j in nums:
                sum += (j >> i) & 1
            if sum % 3 == 1:
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans = ans | (1 << i)
        return ans


# TODO better
print(Solution().singleNumber([-2,-2,1,1,4,1,4,4,-4,-2]))
print(Solution().singleNumber([2,2,3,2]))
print(Solution().singleNumber([0,1,0,1,0,1,99]))
