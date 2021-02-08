class Solution:
    @staticmethod
    def solve(s):
        n = len(s)
        r = 0
        for i in range(n):
            if "0" <= s[i] < "9":
                r = (r * 10) + (ord(s[i]) - ord("0"))
        return r


print(Solution.solve("4568464"))
