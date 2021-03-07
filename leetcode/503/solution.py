from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        index_nums = []
        for i in range(n):
            index_nums.append((i, nums[i]))
        index_nums.sort(key=lambda x: (x[1], -x[0]))
        ans = []
        for i in range(n):
            l = 0
            r = n - 1
            while l <= r:
                mid = l + (r-l)//2
                if nums[i] < index_nums[mid][1]:
                    r = mid - 1
                elif nums[i] > index_nums[mid][1]:
                    l = mid + 1
                else:
                    while mid + 1 < n and nums[i] == index_nums[mid+1][1]:
                        mid += 1
                    break
            if mid + 1 == n:
                ans.append(-1)
            else:
                f_list = list(filter(lambda x: x[0] > i, index_nums[mid + 1:]))
                if len(f_list) == 0:
                    m = min(index_nums[mid + 1:], key=lambda x: x[0])
                else:
                    m = min(f_list, key=lambda x: x[0])
                ans.append(m[1])
        return ans

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ans = [-1] * n
        for i in range(2*n - 1):
            while len(stack) != 0 and nums[i % n] > nums[stack[-1]]:
                ans[stack.pop(-1)] = nums[i % n]
            stack.append(i % n)
        return ans


print(Solution().nextGreaterElements([5,4,3,2,1]))
# print(Solution().nextGreaterElements([1,2,1]))
# print(Solution().nextGreaterElements([1, 5, 5, 4]))
# 1438 单调队列上次也没做出来
