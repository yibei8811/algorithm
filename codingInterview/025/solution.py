class Solution:
    @staticmethod
    def solve(list1, list2):
        result = []
        while True:
            val1 = -1
            val2 = -1
            if len(list1) > 0:
                val1 = list1[0]
            if len(list2) > 0:
                val2 = list2[0]
            if len(list1) == 0 and len(list2) == 0:
                break
            if (len(list1) != 0 and val1 < val2) or len(list2) == 0:
                result.append(list1.pop(0))
            else:
                result.append(list2.pop(0))
        return result


# 归并排序
list1 = [1,3,5,7,9]
list2 = [2,4,6,8]
print(Solution.solve(list1,list2))
