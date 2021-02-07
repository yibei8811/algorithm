class Solution:
    @staticmethod
    def solve(lst):
        n = len(lst)
        lst.sort()
        p = 0
        while lst[p] == 0:
                p += 1
        zero = p
        gap = 0
        while p < n-1:
            if lst[p+1] - lst[p] == 0:
                return False
            else:
                gap += (lst[p+1] - lst[p] - 1)
            p += 1
        return gap <= zero


lst = [7,9,4,0,0]
print(Solution.solve(lst))
