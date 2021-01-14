class Solution:
    @staticmethod
    def solve(lst, start, end, k):
        mid = Solution.partition(lst, start, end)
        if mid == k:
            return lst[0:k]
        elif mid > k:
            return Solution.solve(lst, start, mid-1, k)
        else:
            return Solution.solve(lst, mid+1, end, k)


    # 填坑法
    @staticmethod
    def partition(lst, start, end):
        val = lst[start]
        while start < end:
            # while lst[end] >= val  和  while lst[start] < val 决定切分值相等的数放左边还是右边
            while lst[end] >= val and start < end:
                end -= 1
            lst[start] = lst[end]
            while lst[start] < val and start < end:
                start += 1
            # 最差情况没找到 start == end 退出
            lst[end] = lst[start]
        # 无论如何 start == end 退出后 当前start为坑位index，
        # 哪怕第一次就没找到，自己填自己
        lst[start] = val
        # print(lst)
        return start


lst = [4,5,1,6,2,7,3,8]
print(Solution.solve(lst, 0, len(lst)-1, 4))
# TODO partition() other method
