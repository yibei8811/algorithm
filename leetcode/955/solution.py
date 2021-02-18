from typing import List


class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        count = 0
        for i in range(n-1,-1,-1):
            if A[i] == 0:
                count += 1
                for j in range(0, K):
                    if i-j >= 0:
                        A[i - j] = A[i - j] ^ 1
                    else:
                        return -1
        return count


print(Solution().minKBitFlips([0,1,0], 1))
print(Solution().minKBitFlips([1,1,0], 2))
print(Solution().minKBitFlips([0,0,0,1,0,1,1,0], 3))