class MyQueue:

    def __init__(self):
        self.stack_main = []
        self.stack_help = []

    def push(self, x: int) -> None:
        self.stack_main.append(x)

    # 官方有更好的解法不用复原
    def pop(self) -> int:
        while len(self.stack_main) > 0:
            self.stack_help.append(self.stack_main.pop(0))
        val = self.stack_help.pop(0)
        while len(self.stack_help) > 0:
            self.stack_main.append(self.stack_help.pop(0))
        return val

    def peek(self) -> int:
        while len(self.stack_main) > 0:
            self.stack_help.append(self.stack_main.pop(0))
        val = self.stack_help[0]
        while len(self.stack_help) > 0:
            self.stack_main.append(self.stack_help.pop(0))
        return val

    def empty(self) -> bool:
        return len(self.stack_main) == 0


obj = MyQueue()
print(obj.push(1))
print(obj.push(2))
print(obj.peek())
print(obj.pop())
print(obj.empty())
