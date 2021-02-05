class Solution:
    @staticmethod
    def solve(ch):
        n = len(ch)
        p1 = p2 = n
        res = ''
        while p1 >= 0:
            p1 -= 1
            if ch[p1] == ' ':
                if p2 == n:
                    res = ch[p1 + 1:p2]
                else:
                    res += ch[p1:p2]
                p2 = p1
        return res + ' ' + ch[:p2]


s = 'I am a student.'
print(Solution.solve(s))
