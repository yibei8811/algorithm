class Solution:
    @staticmethod
    def solve(arr, key):
        x = len(arr)
        y = len(arr[0])
        for vx in range(x):
            for vy in range(y):
                print(str(vx)+":"+str(vy))
                if arr[vx][vy] == key:
                    return True
                elif arr[vx][vy] > key:
                    y = vy
                    if y <= 0:
                        return False
                    continue
        return False


print(Solution.solve([[1,3,4,9],
                      [2,4,5,10],
                      [3,6,7,11]], 100))
print(Solution.solve([[1,3,4,9],
                      [2,4,5,10],
                      [3,6,7,11]], 0))
print(Solution.solve([[1,3,4,9],
                      [2,4,5,10],
                      [3,6,7,11]], 6))


