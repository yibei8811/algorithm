class Solution:
    @staticmethod
    def solve(lst, k):
        count = k
        start = -1
        while len(lst) > 1:
            if count == 0:
                lst.pop(start)
                start -= 1
                count = k
            else:
                count -= 1
                if start + 1 < len(lst):
                    start += 1
                else:
                    start = 0
        return lst.pop(0)


# TODO book 逆映射
lst = [0,1,2,3,4]
print(Solution.solve(lst, 3))
