class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 0
        ans = 0
        while i < 32:
            if n & (1 << i) != 0:
                ans += 1
            i += 1
        return ans


print(Solution().hammingWeight(0b00000000000000000000000000001011))
print(Solution().hammingWeight(0b00000000000000000000000010000000))
print(Solution().hammingWeight(0b11111111111111111111111111111101))
