# https://leetcode-cn.com/problems/permutation-in-string/
import time


class Solution:

    # 暴力
    def checkInclusion1(self, s1: str, s2: str) -> bool:
        all = []
        self.allstr('', [], s1, all)
        n = len(all)
        for i in range(0, n):
            if all[i] in s2:
                return True
        return False

    def allstr(self, cur, use, s1, all):
        if len(cur) == len(s1):
            all.append(cur)
            return
        n1 = len(s1)
        for i in range(0, n1):
            if i not in use:
                use.append(i)
                self.allstr(cur + s1[i], use, s1, all)
                use.remove(i)

    # s1是否都能插入s2,对应坐标位置，且坐标位置排序后，符合顺序
    def checkInclusion2(self, s1: str, s2: str) -> bool:
        all = []
        self.serch(s1, s2, [], all, 0, len(s1))
        for i in range(0, len(all)):
            all[i].sort()
            pre = None
            sum = 1
            for i in all[i]:
                if pre is None:
                    pre = i
                else:
                    if i == pre + 1:
                        pre = i
                        sum += 1
                    else:
                        continue
                if sum == len(s1):
                    return True
        return False

    def serch(self, s1, s2, use, all, min, max):
        index = s2.find(s1[0])
        while index != -1:
            if index not in use:
                if min == 0 or index - min < max:
                    use.append(index)
                    if len(s1) > 1:
                        self.serch(s1[1:], s2, use, all, index if index < min else min, max)
                    else:
                        all.append(use[:])
                    use.remove(index)
            index = s2.find(s1[0], index + 1)

    # double pointer
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        win = {}
        for i in s1:
            if i not in win:
                win[i] = 1
            else:
                win[i] += 1
        p = q = 0
        while q < n2:
            if s2[q] in win:
                win[s2[q]] -= 1
            else:
                win[s2[q]] = -1
            while win[s2[q]] < 0 and p <= q:
                if s2[p] not in win:
                    win[s2[p]] = 1
                else:
                    win[s2[p]] += 1
                p += 1
            if q-p+1 == n1:
                return True
            else:
                q += 1
        return False



print(Solution().checkInclusion('trinitrophenylmethylnitramine', 'dinitrophenylhydrazinetrinitrophenylmethylnitramine'))
print(Solution().checkInclusion('ab', 'eidbaooo'))
print(Solution().checkInclusion('ab', 'eidboaoo'))
