from functools import cmp_to_key


class Solution:
    @staticmethod
    def fun(x, y):
        if x[1]['count'] != y[1]['count']:
            return x[1]['count'] - y[1]['count']
        if x[1]['count'] == y[1]['count']:
            return x[1]['tik'] - y[1]['tik']

    @staticmethod
    def solve(s):
        tik = 0
        dict = {}
        for i in s:
            tik += 1
            info = dict.get(i)
            if info is None:
                dict[i] = {'tik':tik, 'count':1}
            else:
                dict[i] = {'tik':tik, 'count':info['count'] + 1}
        return sorted(list(dict.items()), key=cmp_to_key(Solution.fun))


print(Solution.solve('abaccdeff'))
