class Solution:
    @staticmethod
    def solve(n):
        return n and (n + Solution.solve(n - 1))


# 参考https://zhuanlan.zhihu.com/p/64698425
print(Solution.solve(100))
