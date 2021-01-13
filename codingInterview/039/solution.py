class Solution:
    @staticmethod
    def solve(lst):
        n = len(lst)//2
        dict = {}
        for tmp in lst:
            if dict.get(tmp) is None:
                dict[tmp] = 1
            else:
                dict[tmp] += 1
            if dict[tmp] > n:
                return tmp


lst = [1,2,3,2,2,2,5,4,2]
print(Solution.solve(lst))
# https://segmentfault.com/a/1190000004410119
# TODO test quickstart split method
