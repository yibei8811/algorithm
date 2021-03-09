class Solution:
    def removeDuplicates(self, S: str) -> str:
        res = []
        n = len(S)
        for i in range(n):
            if len(res) == 0 or res[-1] != S[i]:
                res.append(S[i])
            else:
                res.pop(-1)
        return "".join(res)


print(Solution().removeDuplicates("abbaca"))
