class Solution:
    def calculate(self, s: str) -> int:
        stackOp = []
        stackVal = []
        s = s.replace(' ','')
        f_next = self.next(s)
        while True:
            v = f_next()
            if v is None and len(stackVal) == 1:
                if len(stackOp) > 0 and stackOp.pop(-1) == '-':
                    return stackVal.pop(-1)*-1
                return stackVal.pop(-1)
            while v == ')' or v is None:
                if v is None and len(stackVal) == 1:
                    return stackVal.pop(-1)
                op = stackOp.pop(-1)
                if op == '(':
                    break
                else:
                    if v is None and len(stackVal) == 1:
                        if len(stackOp) > 0 and stackOp.pop(-1) == '-':
                            return stackVal.pop(-1) * -1
                        return stackVal.pop(-1)
                    v2 = stackVal.pop(-1)
                    v1 = stackVal.pop(-1)
                    if op == '+':
                        stackVal.append(v1 + v2)
                    if op == '-':
                        stackVal.append(v1 - v2)
            if (v.startswith('-') and v[1:] or v).isdigit():
                stackVal.append(int(v))
            elif v == ' ':
                pass
            elif v == '(':
                stackOp.append(v)
            elif v in ['+','-']:
                if len(stackOp) > 0 and stackOp[-1] in ['+','-']:
                    op = stackOp.pop(-1)
                    v2 = stackVal.pop(-1)
                    v1 = stackVal.pop(-1)
                    if op == '+':
                        stackVal.append(v1 + v2)
                    elif op == '-':
                        stackVal.append(v1 - v2)
                stackOp.append(v)

    def next(self,s) -> str:
        l = 0
        r = 0
        def call():
            nonlocal l
            nonlocal r
            ans = None
            if l < len(s):
                while r < len(s) and \
                        ((s[l].isdigit() and s[r].isdigit()) or
                         (r == l) or
                         (s[l] == '-' and s[r].isdigit()
                            and (l == 0 or (l-1 >= 0 and (s[l-1] in ['+','-']))))
                         ):
                    r += 1
                ans = s[l:r]
                l = r
            return ans
        return call


# print(Solution().calculate("1 + 1"))
# print(Solution().calculate("2-1 + 2"))
# print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))
# print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))
print(Solution().calculate("- (3 + (4 + 5))"))
