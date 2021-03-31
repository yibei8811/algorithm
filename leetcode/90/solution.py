from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return [[]]
        ans = [[nums[0]]]
        subset = self.subsetsWithDup(nums[1:])
        for s in subset:
            # 排序保证子集有序
            t = s[:]
            t.sort()
            if t not in ans:
                ans.append(t)
            s.insert(0,nums[0])
            t = s[:]
            t.sort()
            if t not in ans:
                ans.append(t)
        return ans


# n位的子集
# 等于 第一位 与 后面n-1的子集进行拼接和不拼接
# print(Solution().subsetsWithDup([1,2,3]))
# print(Solution().subsetsWithDup([1,2,2]))
# print(Solution().subsetsWithDup([0]))
