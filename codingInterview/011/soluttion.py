class Solution:
    @staticmethod
    def solve(lst):
        if lst[0] < lst[-1]:
            return lst[0]
        else:
            left = 0
            right = len(lst)-1
            while right - left > 0:
                if right - left == 1:
                    if lst[left] <= lst[right]:
                        return lst[left]
                    else:
                        return lst[right]
                pos = (right-left)//2
                if lst[left+pos] > lst[right]:
                    left = left + pos
                else:
                    right = right - pos
        pass


print(Solution.solve([3,4,5,6,7,8,9,1,2,3]))
print(Solution.solve([6,7,8,9,1,2,3,4,5,6]))
print(Solution.solve([1,2,3,4,5,6,7,8,9]))
# 下面需要顺序查找 todo
print(Solution.solve([1,1,1,0,1]))
print(Solution.solve([1,0,1,1,1]))
