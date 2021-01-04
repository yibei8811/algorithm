# see D:\workspaces\worksvn\3.0.2\Test\src\test\Solution.java


class Solution:
    @staticmethod
    def solve(str, pattern):
        n = len(str)
        i = 0
        p = 0
        dp = [0] * n
        while i < n:
            if p >= len(pattern):
                return False
            i_step = 0
            p_step = 0
            if pattern[p] == '.' or pattern[p] == str[i]:
                i_step = 1
                p_step = 1
                dp[i] = 1
            elif pattern[p] == '*':
                if dp[i-1] == 0:  # 解决 * 号可以代表 0
                    dp[i-1] = 1   # * 表示出现0次
                    p_step = 1    # i不变 p++
                elif dp[i-1] == 1 and (str[i] == str[i-1] or pattern[p-1] == '.'):
                    dp[i] = 1
                    i_step = 1
                else:
                    p_step = 1  # i不变 p++
            elif i > 1 and dp[i-1] == 0:
                return False
            else:  # 不匹配 p++ 可能下一个* 代表0次
                p_step = 1
            i += i_step
            p += p_step

        # str match结束后 p未结束，但是存在*表示为0的情况
        pflag = True
        if p < len(pattern):
            if p == len(pattern) - 1 and pattern[p] == '*':
                return True
            for p in range(p, len(pattern)):
                if pattern[p] != '*':
                    if pflag:
                        pflag = False
                    else:
                        return False
                else:
                    pflag = True
        elif p == len(pattern):
            return True
        return pflag


print(Solution.solve("aa", "a"))
print(Solution.solve("aa", "aa"))
print(Solution.solve("aaa", "aa"))
print(Solution.solve("aa", "a*"))
print(Solution.solve("aa", ".*"))
print(Solution.solve("ab", ".*"))
print(Solution.solve("aab", "c*a*b"))
print(Solution.solve("aab", "c*d*a*bd*"))
print(Solution.solve("aab", "c*d*a*b*d*"))
print(Solution.solve("aab", "c*d*a*bd*e"))
