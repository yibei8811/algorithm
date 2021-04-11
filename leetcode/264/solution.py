class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [1]
        n2 = 0
        n3 = 0
        n5 = 0
        while len(ans) < n:
            r = min(ans[n2] * 2, ans[n3] * 3, ans[n5] * 5)
            ans.append(r)
            if r == ans[n2] * 2:
                n2 += 1
            if r == ans[n3] * 3:
                n3 += 1
            if r == ans[n5] * 5:
                n5 += 1
        return ans[n-1]


print(Solution().nthUglyNumber(10))
