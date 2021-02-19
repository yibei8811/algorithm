from typing import List


class Solution:
    # 如果 K = 3，题目可以转换为求每5个0中间的长度
    def longestOnes(self, A: List[int], K: int) -> int:
        # if sum(A) + K >= len(A):
        #     return len(A)
        A.insert(0,0)
        A.append(0)
        n = len(A)
        k = K
        p = 0
        q = 1
        result = 0
        list0_index = []
        for i in range(1, n):
            if A[i] == 0:
                list0_index.append(i)
                if k == 0:
                    q = i
                    result = max(result, q - p - 1)
                    p = list0_index.pop(0)
                else:
                    k -= 1
        return max(result, i - p - 1)

    # right - left 路径上0的个数 > k 的时候 right++, left++
    # right - left 路径上0的个数 <= k right++，left不变
    # right++ 窗口才能变大, 则需要A[left]是0的时候， count--
    def longestOnes2(self, A: List[int], K: int) -> int:
        left,right,count = 0,0,0
        for right in range(len(A)):
            if A[right] == 0:
                count += 1
            if count > K:
                if A[left] == 0:
                    count -= 1
                left += 1
        return right - left + 1


print(Solution().longestOnes2([1,1,1,0,0,0,1,1,1,1,0],2))
print(Solution().longestOnes2([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))
print(Solution().longestOnes2([0,0,0,1],4))
