from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        n = len(weights)
        min_ = max(weights)
        max_ = sum(weights)
        while min_ < max_:
            mid = (max_ + min_) // 2
            d = 0
            count = 0
            for i in range(n):
                if count + weights[i] <= mid:
                    count += weights[i]
                else:
                    count = weights[i]
                    d += 1
            if d >= D:
                min_ = mid + 1
            else:
                max_ = mid
        return min_

