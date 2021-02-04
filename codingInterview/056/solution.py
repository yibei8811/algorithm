from functools import reduce


class Solution:
    @staticmethod
    def solve(lst):
        r = 0
        for i in lst:
            r = r ^ i
        right = 0
        while (r & 1) != 1:
            right += 1
            r = r >> right
        lst1 = []
        lst2 = []
        for i in lst:
            if ((i >> right) & 1) == 1:
                lst1.append(i)
            else:
                lst2.append(i)
        return [reduce(lambda x,y: x ^ y, [_ for _ in lst1]),
                reduce(lambda x, y: x ^ y, [_ for _ in lst2])]


lst = [1,1,6,88,3,3,4,4,5,5,9,9,66,66]
print(Solution.solve(lst))
