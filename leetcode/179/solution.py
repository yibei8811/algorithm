from functools import cmp_to_key
from typing import List


class Solution:
    @staticmethod
    def fun(x, y):
        if x == y:
            return 0
        x = str(x)
        y = str(y)
        if x + y == y + x:
            return 0
        xn = len(x)
        yn = len(y)
        xi = 0
        yi = 0
        while x[xi] == y[yi]:
            xi += 1
            yi += 1
            if xi == xn:
                x = x + x
                xn = xn * 2
            if yi == yn:
                y = y + y
                yn = yn * 2
        return int(y[yi]) - int(x[xi])

    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(nums,key=cmp_to_key(Solution.fun))
        ans = ''
        for i in nums:
            ans += str(i)
        while len(ans) > 1 and ans[0] == '0':
            ans = ans[1:]
        return ans


# print(Solution().largestNumber([10,2]))
# print(Solution().largestNumber([3,30,34,5,9]))
# print(Solution().largestNumber([432,43243]))
# print(Solution().largestNumber([34323,3432]))
# print(Solution().largestNumber([999999991,9]))
# print(Solution().largestNumber([0,0]))
# print(Solution().largestNumber([3,43,48,94,85,33,64,32,63,66]))
# print(Solution().largestNumber([3,34]))
