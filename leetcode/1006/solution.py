class Solution:
    def clumsy(self, N: int) -> int:
        op = '*'
        stack_val = []
        stack_op = []
        pri = {'+':1,'-':1,'*':2,'/':2}
        while True:
            if N == 0:
                if len(stack_val) == 1:
                    return stack_val[0]
                v2 = stack_val.pop(-1)
                v1 = stack_val.pop(-1)
                s_op = stack_op.pop(-1)
                if s_op == '*':
                    stack_val.append(v1 * v2)
                if s_op == '/':
                    stack_val.append(v1 // v2)
                if s_op == '+':
                    stack_val.append(v1 + v2)
                if s_op == '-':
                    stack_val.append(v1 - v2)
            else:
                stack_val.append(N)
                if len(stack_op) == 0:
                    stack_op.append(op)
                else:
                    while len(stack_val) > 1 and (pri.get(op) <= pri.get(stack_op[-1])):
                        v2 = stack_val.pop(-1)
                        v1 = stack_val.pop(-1)
                        s_op = stack_op.pop(-1)
                        if s_op == '*':
                            stack_val.append(v1*v2)
                        elif s_op == '/':
                            stack_val.append(v1//v2)
                        elif s_op == '+':
                            stack_val.append(v1+v2)
                        elif s_op == '-':
                            stack_val.append(v1-v2)
                    stack_op.append(op)
                N -= 1
                if N == 1:
                    op = '+'
                elif op == '*':
                    op = '/'
                elif op == '/':
                    op = '+'
                elif op == '+':
                    op = '-'
                elif op == '-':
                    op = '*'


print(Solution().clumsy(4))
print(Solution().clumsy(10))
