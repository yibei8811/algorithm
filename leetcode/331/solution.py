class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        arr = preorder.split(',')
        n = len(arr)
        stack = [1]
        i = 0
        while i < n:
            if len(stack) == 0:
                return False
            tmp = stack.pop(-1) - 1
            if tmp > 0:
                stack.append(tmp)
            if arr[i] != '#':
                stack.append(2)
            i += 1
        return len(stack) == 0


print(Solution().isValidSerialization("1,#,#"))
