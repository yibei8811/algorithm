class Solution:
    stack1 = []
    stack2 = []

    def push(self, data):
        self.stack1.append(data)
        if len(self.stack2) == 0:
            self.stack2.append(data)
        elif data <= self.stack2[-1]:
            self.stack2.append(data)

    def pop(self):
        if len(self.stack1) > 0:
            data1 = self.stack1[-1]
            data2 = self.stack2[-1]
            if data1 == data2:
                self.stack2.pop()
            return self.stack1.pop()
        return None

    def min(self):
        if len(self.stack2) > 0:
            return self.stack2[-1]
        return None


s = Solution()
s.push(3)
s.push(3)
s.push(1)
s.push(3)
s.push(1)
print("min:"+str(s.min()))
print("pop:"+str(s.pop()))
print("min:"+str(s.min()))
print("pop:"+str(s.pop()))
print("min:"+str(s.min()))
print("pop:"+str(s.pop()))
print("min:"+str(s.min()))
print("pop:"+str(s.pop()))
print("min:"+str(s.min()))
print("pop:"+str(s.pop()))
print("min:"+str(s.min()))
print("pop:"+str(s.pop()))
