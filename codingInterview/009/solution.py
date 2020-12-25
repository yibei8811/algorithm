class Solution:
    stack1 = []
    stack2 = []

    def add(self, data):
        self.stack1.append(data)

    def remove(self):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack2.pop()
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

    def __str__(self):
        return self.stack1.__str__() + ":" + self.stack2.__str__()


solution = Solution()
solution.add(1)
solution.add(2)
solution.add(3)
solution.remove()
solution.add(4)
solution.add(5)
solution.remove()
solution.add(6)
print(solution)

