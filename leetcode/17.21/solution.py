from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        queue = []
        ans = 0
        i = 0
        while i < n:
            if len(queue) == 0 or height[i] <= height[queue[-1]]:
                pass
            elif len(queue) == 1 and height[i] > height[queue[-1]]:
                queue.pop(0)
            elif len(queue) >= 2 and height[i] > height[queue[-1]]:
                h = min(height[queue[-2]], height[i])
                ans += (h - height[queue[-1]]) * (i - queue[-2] - 1)
                queue.pop(-1)
                continue
            queue.append(i)
            i += 1
        return ans


# TODO dp and double pointer
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))







