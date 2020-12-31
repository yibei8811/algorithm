class Solution:
    @staticmethod
    def solve(now,n):
        if n == 0:
            print(str(now))
        else:
            for j in range(0,10):
                Solution.solve(str(now)+str(j),n-1)


Solution.solve('',5)
