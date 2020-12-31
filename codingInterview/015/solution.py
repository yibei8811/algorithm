class Solution:
    @staticmethod
    def solve(n):
        sum = 0
        for i in range(32):
            if n & (1 << i):
                sum += 1
        return sum


print(Solution.solve(9))
print(Solution.solve(10))
print(Solution.solve(11))
print(Solution.solve(12))
