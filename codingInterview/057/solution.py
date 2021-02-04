class Solution:
    @staticmethod
    def solve(lst, k):
        n = len(lst)
        p = 0
        q = n - 1
        while q > p:
            if lst[p] + lst[q] == k:
                return [lst[p], lst[q]]
            if lst[p] + lst[q] > k:
                q -= 1
            else:
                p += 1
        return None


lst = [1,2,4,7,11,15]
print(Solution.solve(lst, 15))
