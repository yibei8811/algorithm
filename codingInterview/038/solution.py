class Solution:
    @staticmethod
    def solve(r, lst):
        if len(r) == len(lst):
            print(r)
        for c in lst:
            if r.find(c) == -1:
                Solution.solve(r+c, lst)


Solution.solve("", "abcd")
# TODO ex combination and 8 queue
