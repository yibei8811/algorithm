import time
class Solution:
    @staticmethod
    def solve(n):
        result = 0
        for i in range(1, n+1):
            quotient = n // i
            remainder = n % i
            product = 1
            for j in range(i):
                if j < remainder:
                    product = product * (quotient+1)
                else:
                    product = product * quotient
            if product > result:
                result = product
        return result

    @staticmethod
    def solve2(n):
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        dp[4] = 4
        for i in range(5,n+1):
            for j in range(1, i):
                if dp[i-j] * dp[j] > dp[i]:
                    dp[i] = dp[i-j]*dp[j]
        return dp[n]


print(time.time())
print(Solution.solve(1000))# best
print(time.time())
print(Solution.solve2(1000))
print(time.time())
