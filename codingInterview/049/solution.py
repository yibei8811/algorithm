class Solution:
    @staticmethod
    def solve(n):
        res = [1]
        p2 = p3 = p5 = 0
        max = 1
        while len(res) < n:
            while res[p2] * 2 <= max:
                p2 += 1
            while res[p3] * 3 <= max:
                p3 += 1
            while res[p5] * 5 <= max:
                p5 += 1
            max = min(res[p2] * 2, res[p3] * 3, res[p5] * 5)
            res.append(max)
        return res


print(Solution.solve(1500))
