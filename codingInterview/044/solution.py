class Solution:
    # 见图
    @staticmethod
    def solve(n):
        divider = 1
        segment = 10
        while n - segment >= 0:
            n -= segment
            divider += 1
            segment = (10**divider - 10**(divider-1)) * divider
        div = n // divider
        mod = n % divider
        # fix 10的0次方等于1 这里需要等于0
        if divider == 1:
            return str(div)[mod]
        return str(10**(divider-1) + div)[mod]

    # see https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/
    @staticmethod
    def solve2(n: int):
        digit, start, count = 1, 1, 9
        while n > count:  # 1.
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit  # 2.
        return str(num)[(n - 1) % digit]  # 3.


for i in range(600000):
    if Solution.solve(i) != str(Solution.solve2(i)):
        print(i)
