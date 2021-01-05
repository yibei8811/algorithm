class Solution:
    @staticmethod
    def solve(arr):
        n = len(arr)
        left = 0
        right = n -1
        while right - left > 1:
            while arr[left] % 2 == 1:
                left += 1
            while arr[right] % 2 == 0:
                right -= 1
            if right - left > 1:
                arr[left] = arr[left] ^ arr[right]
                arr[right] = arr[left] ^ arr[right]
                arr[left] = arr[left] ^ arr[right]
        return arr


arr = [1,2,3,4,5,6,7,8]
print(Solution.solve(arr))
