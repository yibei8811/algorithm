class Solution:
    @staticmethod
    def solve(lst):
        if len(lst) <= 2:
            return True
        root = lst[-1]
        for i in lst:
            if i >= root:
                index = lst.index(i)
                # If the iterable is empty, return True.
                if all([_ > root for _ in lst[index:-1]]) is False:
                    return False
                return Solution.solve(lst[0:index]) and Solution.solve(lst[index:-1])


print(Solution.solve([5,7,6,9,8,10,11]))
print(Solution.solve([1,2,3,7,4,5,6]))
print(Solution.solve([5,7,6,9,11,10,8]))

# print([_ for _ in [5,4,3] if _ > 3])
# [5, 4]
# print([_ > 3 for _ in [5,4,3] if _ > 3])
# [True, True]
# print([5,6,7][2:-1])
# []
