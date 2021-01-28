from functools import cmp_to_key, reduce
import random


class Solution:
    def __init__(self, res):
        self.res = res

    # TODO bfs 这道题，可能拿广度搜索效果会比较好
    # 过大数组有问题
    def dfs(self, lst, visable, pre_char):
        if sum(_ for _ in visable) == len(visable):
            return pre_char
        # 内存递归函数修改不了外层res 所以用self
        # res = '9' * sum(len(str(_)) for _ in lst)
        for i in range(len(lst)):
            if visable[i] == 0:
                visable[i] = 1
                if Solution.compare(pre_char + str(lst[i]), self.res):
                    tmp = self.dfs(lst, visable, pre_char + str(lst[i]))
                    if int(tmp) < int(self.res):
                        self.res = tmp
                visable[i] = 0
        return self.res

    @staticmethod
    def compare(s1, s2):
        l = min(len(s1),len(s2))
        if s1[0:l] <= s2[0:l]:
            return True
        return False

    @staticmethod
    def solve1(lst):
        return Solution('9' * sum(len(str(_)) for _ in lst)).dfs(lst,[0] * len(lst),'')

    @staticmethod
    def solve2(lst):
        # https://www.polarxiong.com/archives/Python3-%E6%89%BE%E5%9B%9Esort-%E4%B8%AD%E6%B6%88%E5%A4%B1%E7%9A%84cmp%E5%8F%82%E6%95%B0.html
        lst = sorted(lst, key=cmp_to_key(Solution.func))
        return reduce(lambda x,y: str(x)+str(y), lst, '')

    @staticmethod
    def func(x, y):
        xy = str(x) + str(y)
        yx = str(y) + str(x)
        if xy < yx:
            return -1
        if xy == yx:
            return 0
        else:
            return 1


for i in range(0,100):
    lst = []
    random.seed(i)
    for i in range(1, random.randrange(1,10)):
        lst.append(random.randrange(1,10))
    s1 = Solution.solve1(lst)
    s2 = Solution.solve2(lst)
    if s1 == s2:
        print(s1)
    else:
        print('fail')
