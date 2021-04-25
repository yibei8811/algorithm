class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        n = len(haystack)
        m = len(needle)
        j = 0
        next = self.next_array(needle)
        for i in range(n):
            while j - 1 >= 0 and haystack[i] != needle[j]:
                j = next[j-1]
            if haystack[i] == needle[j]:
                j += 1
            if j == m:
                return i - j + 1
        return -1

    def next_array(self, needle):
        n = len(needle)
        k = 0
        next = [0] * n
        for i in range(1,n):
            while k - 1 >= 0 and needle[k] != needle[i]:
                k = next[k-1]
            if needle[k] == needle[i]:
                k += 1
            next[i] = k
        return next


print(Solution().strStr('abcdabce','abce'))
