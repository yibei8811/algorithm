class Solution:
    @staticmethod
    def solve(num1, num2):
        while num2 != 0:
            foo = num1 ^ num2
            num2 = (num1 & num2) << 1
            num1 = foo
        return num1


#  想象10进制加法，进位总会结束
print(Solution.solve(99, 88))
