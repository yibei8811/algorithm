class Solution:
    # TODO 有一个优化空间，循环的时候每次都是大一个小一个，那中位数始终不变
    @staticmethod
    def solve(lst):
        mid = [0] * len(lst)
        start = 0
        for index in range(len(lst)):
            if index == 0:
                mid[index] = lst[index]
            else:
                # 偶数列表
                if index % 2 == 1:
                    if lst[index] == mid[index-1]:
                        mid[index] = mid[index-1]
                    elif lst[index] > mid[index-1]:
                        k = Solution.k_largest(lst, start, index, index // 2 + 1)
                        mid[index] = (mid[index - 1] + k) / 2
                    else:
                        k = Solution.k_largest(lst, start, index, index // 2)
                        mid[index] = (mid[index - 1] + k) / 2
                else:
                    mid[index] = Solution.k_largest(lst, start, index, index // 2)
        return mid


    @staticmethod
    def k_largest(lst, start, end, k):
        index = Solution.partition(lst, start, end)
        if index == k:
            return lst[k]
        elif index < k:
            return Solution.k_largest(lst, index+1, end, k)
        else:
            return Solution.k_largest(lst, start, index-1, k)

    # 交换法
    @staticmethod
    def partition(lst, start, end):
        key = start
        val = lst[start]
        start += 1
        # <= 用于区分指针退出，还是找到index
        while start <= end:
            while lst[start] < val and start <= end:
                start += 1
            while lst[end] >= val and start <= end:
                end -= 1
            if start < end:
                lst[start] = lst[start] ^ lst[end]
                lst[end] = lst[start] ^ lst[end]
                lst[start] = lst[start] ^ lst[end]
        # 当 start > end时候
        # 证明start左边小于val 既end小于val
        # 所以lst[end] 和 lst[key] 互换
        # key 不能等于 end 不然只有一个变量，无法完成替换
        if key != end:
            lst[key] = lst[key] ^ lst[end]
            lst[end] = lst[key] ^ lst[end]
            lst[key] = lst[key] ^ lst[end]
        # 注意是返回 end
        return end


lst = [3,23,1,8,9,3,2,3,2]
print(Solution.solve(lst))
# TODO max/min heap
# 中位数为什么是O(n),大概是因为数据流，每一个数都查中位数，所以平均是O(n)
# TODO try again
