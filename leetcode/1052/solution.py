from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        p = 0
        q = X
        ans = 0
        now = 0
        for i in range(p, q):
            if grumpy[i] == 1:
                now += customers[i]
        ans = now
        while q < n:
            count = 0
            if grumpy[q] == 1:
                count += customers[q]
            if grumpy[p] == 1:
                count -= customers[p]
            now += count
            if now > ans:
                ans = now
            q += 1
            p += 1
        for i in range(n):
            if grumpy[i] == 0:
                ans += customers[i]
        return ans


print(Solution().maxSatisfied([1,0,1,2,1,1,7,5],[0,1,0,1,0,1,0,1],3))
print(Solution().maxSatisfied([1],[0],1))
print(Solution().maxSatisfied([10,1,7],[0,0,0],2))
