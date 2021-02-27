class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        start = 0
        end = n
        dict = {}
        for (index, c) in enumerate(s):
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
        indexs = []
        for (index, c) in enumerate(s):
            if dict[c] < k:
                indexs.append(index)
        if len(indexs) == 0:
            return end - start
        else:
            ans = 0
            start = 0
            while len(indexs) > 0:
                idx = indexs.pop(0)
                ans = max(ans, self.longestSubstring(s[start:idx], k))
                start = idx + 1
            ans = max(ans, self.longestSubstring(s[idx+1:end], k))
            return ans


# print(Solution().longestSubstring("aaabb",3))
# print(Solution().longestSubstring("ababbc",2))
print(Solution().longestSubstring("aaaaaaaaaaaabcdefghijklmnopqrstuvwzyz", 3))
