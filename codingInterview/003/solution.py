class Solution:
    @staticmethod
    def solve(arr):
        dic = {}
        for var in arr:
            if dic.get(str(var)) is None:
                dic[str(var)] = 1
            else:
                return var
        return dic


print(Solution.solve([1,3,4,5,6,7]))
print(Solution.solve([1,3,4,5,6,6,7]))
print(Solution.solve([]))
