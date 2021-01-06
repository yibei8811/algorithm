class Solution:
    @staticmethod
    def solve(arr):
        m = len(arr[0])
        n = len(arr)
        Solution.rigth(arr, m, n, 0, 0, 0, 0)

    @staticmethod
    def rigth(arr, m, n, x, y, mcount, ncount):
        for i in range(m - mcount):
            print(arr[x][y+i])
        ncount += 1
        if ncount < n:
            Solution.down(arr, m, n, x+1, y+i, mcount, ncount)

    @staticmethod
    def down(arr, m, n, x, y, mcount, ncount):
        for i in range(n - ncount):
            print(arr[x+i][y])
        mcount += 1
        if mcount < m:
            Solution.left(arr, m, n, x+i, y-1, mcount, ncount)

    @staticmethod
    def left(arr, m, n, x, y, mcount, ncount):
        for i in range(m - mcount):
            print(arr[x][y-i])
        ncount += 1
        if ncount < n:
            Solution.up(arr, m, n, x-1, y-i, mcount, ncount)

    @staticmethod
    def up(arr, m, n, x, y, mcount, ncount):
        for i in range(n - ncount):
            print(arr[x-i][y])
        mcount += 1
        if mcount < m:
            Solution.rigth(arr, m, n, x-i, y+1, mcount, ncount)


arr = [['a', 'b', 't', 'g'],
       ['c', 'f', 'c', 's'],
       ['c', '1', '2', 's'],
       ['j', 'd', 'e', 'h']]
arr2 = [['a', 'b', 't', 'g','5'],
        ['c', 'f', 'c', 's','4'],
        ['c', '1', '2', 's','3'],
        ['j', 'd', 'e', 'h','2'],
        ['j', 'd', 'e', 'h','1']]
Solution.solve(arr)
# Solution.solve(arr2)
# TODO better Test
