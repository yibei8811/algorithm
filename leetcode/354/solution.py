from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

    def maxEnvelopes2(self, envelopes: List[List[int]]) -> int:
        n = envelopes.__len__()
        # (2)位必须倒叙，保证sort后 当(1)位的相同的时候，(2)位不会导致增加个数
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # d 表示len长度的，最小的末位数
        d = [envelopes[0][1]]
        len = 1
        for l in range(1,n):
            # 想要替换最后一个，必须小于最后一个，并且大于最后一个前一个
            # 同理 其他
            if envelopes[l][1] > d[len-1]:
                d.append(envelopes[l][1])
                len += 1
            else:
                left = 0
                right = len - 1
                while left < right:
                    mid = left + (right - left)//2
                    if envelopes[l][1] > d[mid]:
                        left = mid + 1
                    else:
                        right = mid
                d[left] = envelopes[l][1]
        return len


# why max(dp[i], dp[j]+1)
# becase [[3, 4], [12, 15], [12, 2], [30, 50]]
print(Solution().maxEnvelopes2([[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]))
print(Solution().maxEnvelopes2([[1,2],[2,3],[3,4],[4,5],[5,6],[5,5],[6,7],[7,8]]))
print(Solution().maxEnvelopes2([[30,50],[12,2],[3,4],[12,15]]))
print(Solution().maxEnvelopes2([[5,4],[6,4],[6,7],[2,3]]))
print(Solution().maxEnvelopes2([[4,5],[4,6],[6,7],[2,3],[1,1]]))
