from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A)
        m = len(A[0])
        for i in range(n):
            for j in range((m+1)//2):
                if A[i][j] != A[i][m-j-1]:
                    A[i][j] = A[i][j] ^ A[i][m-j-1]
                    A[i][m-j-1] = A[i][j] ^ A[i][m-j-1]
                    A[i][j] = A[i][j] ^ A[i][m-j-1]
                A[i][j] ^= 1
                if m-j-1 != j:
                    A[i][m-j-1] ^= 1
        return A


print(Solution().flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
print(Solution().flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
