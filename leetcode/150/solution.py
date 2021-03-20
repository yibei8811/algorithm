from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []
        for i in tokens:
            if i == '+':
                v1 = stack.pop(-1)
                v2 = stack.pop(-1)
                stack.append(v2 + v1)
            elif i == '-':
                v1 = stack.pop(-1)
                v2 = stack.pop(-1)
                stack.append(v2 - v1)
            elif i == '*':
                v1 = stack.pop(-1)
                v2 = stack.pop(-1)
                stack.append(v2 * v1)
            elif i == '/':
                v1 = stack.pop(-1)
                v2 = stack.pop(-1)
                # v2 / v1 和 v2 // v1
                stack.append(int(v2 / v1))
            else:
                stack.append(int(i))
        return stack.pop(0)


# print(Solution().evalRPN(["2","1","+","3","*"]))
# print(Solution().evalRPN(["4","13","5","/","+"]))
print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
