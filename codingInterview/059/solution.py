class Solution:
    @staticmethod
    def solve(lst, k):
        n = len(lst)
        p1 = 1
        p2 = 0
        max = 0
        while p2 < k:
            if lst[p2] > max:
                max = lst[p2]
            p2 += 1
        res = [max]
        while p2 < n:
            if lst[p2] >= max:
                max = lst[p2]
            else:
                max = 0
                tmp = p1
                while tmp <= p2:
                    if lst[tmp] > max:
                        max = lst[tmp]
                    tmp += 1
            res.append(max)
            p1 += 1
            p2 += 1
        return res


# TODO 书上的写法更好，可以学习
lst = [2,3,4,2,6,2,5,1]
print(Solution.solve(lst, 3))
