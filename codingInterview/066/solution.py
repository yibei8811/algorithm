class Solution:
    @staticmethod
    def solve(lst):
        n = len(lst)
        r = [1] * n
        dp1 = [0] * n
        dp1[0] = lst[0]
        for i in range(1, n):
            dp1[i] = dp1[i-1] * lst[i]
        dp2 = [0] * n
        dp2[n-1] = lst[n-1]
        for i in reversed(range(0, n-1)):
            dp2[i] = dp2[i+1] * lst[i]
        for i in range(0, n):
            if i - 1 >= 0:
                r[i] *= dp1[i-1]
            if i + 1 < n:
                r[i] *= dp2[i+1]
        return r


lst = [6,9,1]
print(Solution.solve(lst))

