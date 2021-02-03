class Solution:
    @staticmethod
    def merge_sort(lst, start, end):
        result = []
        if end - start > 0:
            index = start + (end-start)//2
            l1 = Solution.merge_sort(lst, start, index)
            l2 = Solution.merge_sort(lst, index+1, end)
            p = 0
            q = 0
            while p < len(l1) or q < len(l2):
                if p == len(l1):
                    result.append(l2[q])
                    q += 1
                elif q == len(l2):
                    result.append(l1[p])
                    p += 1
                else:
                    if l1[p] < l2[q]:
                        result.append(l1[p])
                        p += 1
                    else:
                        result.append(l2[q])
                        q += 1
            return result
        else:
            result.append(lst[start])
            return result

    @staticmethod
    def solve(lst, start, end):
        s = Solution()
        s.analysis(lst, start, end)
        return s.count

    def __init__(self, count=0):
        self.count = count

    def analysis(self, lst, start, end):
        if end - start > 0:
            index = start + (end - start)//2
            l1 = self.analysis(lst, start, index)
            l2 = self.analysis(lst, index+1, end)
            result = [0] * (len(l1) + len(l2))
            p = len(result) - 1
            p1 = len(l1) - 1
            p2 = len(l2) - 1
            while p >= 0:
                if p1 < 0:
                    result[p] = l2[p2]
                    p2 -= 1
                elif p2 < 0:
                    result[p] = l1[p1]
                    p1 -= 1
                else:
                    if l1[p1] > l2[p2]:
                        result[p] = l1[p1]
                        p1 -= 1
                        self.count += (p2+1)
                    else:
                        result[p] = l2[p2]
                        p2 -= 1
                p -= 1
            return result
        else:
            return [lst[start]]


# 归并排序
lst = [7,5,6,4]
print(Solution.merge_sort(lst, 0, len(lst)-1))
print(Solution.solve(lst, 0, len(lst)-1))
