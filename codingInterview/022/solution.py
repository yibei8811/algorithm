class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Solution:
    def __init__(self, count=0, result=None):
        self.count = 0
        self.result = None

    def solve(self, node, n):
        if node.next is None:
            return
        self.solve(node.next, n)
        self.count += 1
        if self.count == n:
            self.result = node.next.data
        return self.result


node1 = ListNode(1)
node2 = ListNode(2,node1)
node3 = ListNode(3,node2)
node4 = ListNode(4,node3)
print(Solution().solve(node4, 1))
print(Solution().solve(node4, 2))
print(Solution().solve(node4, 3))
# print(Solution().solve(node4, 4)) #TODO

#  a --> b  --> c --> d --> e
#  a <-- b <--  c(求出解,bug,a、b函数继续出栈) <--...
