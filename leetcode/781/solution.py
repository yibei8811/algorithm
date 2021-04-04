from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        n = len(answers)
        if n == 0:
            return 0
        answers.sort()
        dp = [0] * n
        pre = 0
        now = 0
        for i in range(n):
            if answers[i] == pre and now > 0:
                now -= 1
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i - 1] + answers[i] + 1
                pre = answers[i]
                now = answers[i]
        return dp[n-1]


print(Solution().numRabbits([1, 1, 2]))
print(Solution().numRabbits([10, 10, 10]))
print(Solution().numRabbits([]))
