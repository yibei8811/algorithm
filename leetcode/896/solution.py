from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        positive = None
        pre = None
        for i in A:
            if pre is None:
                pass
            elif positive is None:
                if i > pre:
                    positive = 1
                elif i < pre:
                    positive = 0
            else:
                if positive == 1:
                    if i < pre:
                        return False
                else:
                    if i > pre:
                        return False
            pre = i
        return True


print(Solution().isMonotonic([1,2,5,3,3]))
print(Solution().isMonotonic([1,2,2,3]))
print(Solution().isMonotonic([6,5,4,4]))
print(Solution().isMonotonic([1,3,2]))
print(Solution().isMonotonic([1,2,4,5]))
print(Solution().isMonotonic([1,1,1]))
