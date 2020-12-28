direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]
arr = [['a', 'b', 't', 'g'],
       ['c', 'f', 'c', 's'],
       ['j', 'd', 'e', 'h']]
n = len(arr)
m = len(arr[0])


class Solution:

    @staticmethod
    def solve(arr, search):
        for i in range(n):
            for j in range(m):
                now = 0
                useable = [[0] * m for _ in range(n)]
                flag = Solution.bfs(arr, i, j, useable, search, now)
                if flag:
                    print(useable)
                    return True
        return False

    @staticmethod
    def bfs(arr, i, j, useable, search, now):
        if now == len(search):
            return True
        if arr[i][j] == search[now]:
            useable[i][j] = 1
            for pos in direction:
                i += pos[0]
                j += pos[1]
                now += 1
                if 0 <= i < n and 0 <= j < m and useable[i][j] == 0:
                    if Solution.bfs(arr, i, j, useable, search, now):
                        return True
                i -= pos[0]
                j -= pos[1]
                now -= 1
        return False


print(Solution.solve(arr, 'aat'))
print(Solution.solve(arr, 'abfc'))
print(Solution.solve(arr, 'bfct'))
print(Solution.solve(arr, 'csh'))
