class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        result = []
        return self.dfs(result)

    def dfs(self, result):
        if self.next is None:
            result.append(self.data)
            return result.__str__()
        result.append(self.data)
        return self.next.dfs(result)


class Solution:
    def __init__(self, count=0, result=None):
        self.count = 0
        self.result = None

    def solve(self, node, pre_node=None):
        if node is None:
            return
        self.solve(node.next, node)
        self.count += 1
        if self.count == 1:
            self.result = node
        # 原头节点要指向None
        node.next = pre_node
        return self.result


node1 = ListNode(1)
node2 = ListNode(2,node1)
node3 = ListNode(3,node2)
node4 = ListNode(4,node3)
print(node4)
print(Solution().solve(node4))
# 和 022 类似，利用调用栈 LIFO 特性，反向解决
