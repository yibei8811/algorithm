class Solution:
    # 整个过程为 决定子串的开头和结尾
    @staticmethod
    def solve(lst):
        max = 0  # 从头开始累加，如果max变为负数，可以遗忘以前子串
        normal = 1
        normal_total = 0  # 从负号开始查找，累加为正可以进行合并
        for i in range(0, len(lst)):
            if normal == 1:
                if lst[i] >= 0:
                    max += lst[i]
                else:
                    if max + lst[i] < 0:
                        max = 0
                    else:
                        normal = 0
                        normal_total = lst[i]
            else:
                normal_total += lst[i]
                if normal_total > 0:
                    max += normal_total
                    normal = 1
        return max

    @staticmethod
    def solve2(lst):
        n = len(lst)
        dp = [0] * n
        dp[0] = lst[0]
        max = 0
        for i in range(1, n):
            if dp[i-1] < 0:
                dp[i] = lst[i]
            else:
                dp[i] = lst[i] + dp[i-1]
                if dp[i] > max:
                    max = dp[i]
        return max


lst = [1,-2,3,10,-4,7,2,-5]
print(Solution.solve(lst))
print(Solution.solve2(lst))
