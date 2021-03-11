# copy from 224
class Solution:
    def calculate(self, s: str) -> int:
        stackOp = []
        stackVal = []
        s = s.replace(' ','')
        f_next = self.next(s)
        pri = {'+':2,'-':2,
               '*':3,'/':3,
               '(':1,')':1}
        b = True
        while True:
            if b:
                v = f_next()
            if v is None and len(stackVal) == 1:
                if len(stackOp) > 0 and stackOp.pop(-1) == '-':
                    return stackVal.pop(-1)*-1
                return stackVal.pop(-1)
            if v is not None and (v.startswith('-') and v[1:] or v).isdigit():
                stackVal.append(int(v))
            elif v is not None and v == '(':
                stackOp.append(v)
            else:
                if v is None or (len(stackOp) > 0 and pri.get(v) <= pri.get(stackOp[-1])):
                    b = False
                    if stackOp[-1] == '(' and v == ')':
                        stackOp.pop(-1)
                        b = True
                    else:
                        op = stackOp.pop(-1)
                        v2 = stackVal.pop(-1)
                        v1 = stackVal.pop(-1)
                        if op == '+':
                            stackVal.append(v1 + v2)
                        elif op == '-':
                            stackVal.append(v1 - v2)
                        if op == '/':
                            stackVal.append(v1 // v2)
                        if op == '*':
                            stackVal.append(v1 * v2)
                else:
                    b = True
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


print(Solution().calculate("1*2-3/4+5*6-7*8+9/10"))
print(Solution().calculate("3+2*2"))
print(Solution().calculate(" 3/2"))
print(Solution().calculate("3+5 / 2"))


