class Solution:
    @staticmethod
    def solve(lst):
        n = len(lst)
        dp = [0] * n
        dp[0] = 0
        min = lst[0]
        for i in range(1, n):
            if lst[i] < min:
                min = lst[i]
            dp[i] = max(dp[i-1], lst[i] - min)
        return dp[n-1]


lst = [9,11,8,5,7,12,16,14]
print(Solution.solve(lst))
# TODO 对股票市场分析，平均涨幅多久卖出比较合适
