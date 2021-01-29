class Solution:
    @staticmethod
    def solve(n, s, res):
        if len(n) == 0:
            return res.append(s)
        Solution.solve(n[1:], s + ',' + n[0], res)
        if len(n) > 1 and int(n[0:2]) < 26:
            Solution.solve(n[2:], s + ',' + n[0:2], res)
        return res


print(Solution.solve('12258', '', []))
# TODO 书上代码画图
