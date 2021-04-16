from functools import lru_cache


class Solution:
    @lru_cache(10000)
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if s1 == s2:
            return True
        if n == 1:
            return s1 == s2
        ans = False
        for i in range(1,n):
            # print(s1[0:i], s2[0:i])
            # print(s1[i:], s2[i:])
            # print(s1[0:i], s2[n-i:])
            # print(s1[i:], s2[0:n-i])
            ans = ans or (
                    (self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i:], s2[i:])) \
                  or (self.isScramble(s1[0:i], s2[n-i:]) and self.isScramble(s1[i:], s2[0:n-i]))
            )
        return ans


# print(Solution().isScramble('abcdefghijklmnopq','efghijklmnopqcadb'))
# print(Solution().isScramble('abc','bca'))
# print(Solution().isScramble('great','rgeat'))
# print(Solution().isScramble('abcde','caebd'))
