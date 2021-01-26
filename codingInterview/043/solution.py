class Solution:

    # 每一位 出现数字1的个数相加
    @staticmethod
    def solve(str):
        n = len(str)
        sum = 0
        coefficient = 1
        for i in range(n-1, -1, -1):
            bit = int(str[i])
            prefix = int("0" if str[0:i] == "" else str[0:i])
            suffix = int("0" if str[i+1:] == "" else str[i+1:])
            sum += (prefix * coefficient)
            if bit > 1:
                sum += coefficient
            elif bit == 1:
                sum = sum + suffix + 1
            coefficient *= 10
        return sum


print(Solution.solve("21340"))
# 书上的解释非常难理解，思路应该是数字分段累加，解释看上去比较懵的，下面的解释略好
# TODO https://zhuanlan.zhihu.com/p/34840919
