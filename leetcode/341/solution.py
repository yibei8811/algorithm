class NestedIterator:
    def __init__(self, nestedList):
        self.data = nestedList
        self.n = len(nestedList)
        self.count = 0
        self.it = None

    def next(self) -> int:
        if type(self.data[self.count]) == type(1):
            ans = self.data[self.count]
            self.count += 1
            return ans
        else:
            return self.it.next()

    def hasNext(self) -> bool:
        if self.count == self.n:
            return False
        if type(self.data[self.count]) == type(1):
            return True
        else:
            if self.it is None:
                self.it = NestedIterator(self.data[self.count])
            if self.it.hasNext() is True:
                return True
            if self.count < self.n - 1:
                self.count += 1
                self.it = None
                return self.hasNext()
            else:
                return False


v = []
# it = NestedIterator([1, [], 3, [4,[5,[6,7]]],[8],[]])
it = NestedIterator([[],[]])
while it.hasNext():
    v.append(it.next())
print(v)
