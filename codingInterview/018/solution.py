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
    @staticmethod
    def solve(head, node):
        if node.next is not None:
            next_node = node.next
            node.data = next_node.data
            node.next = next_node.next
            # clear
            next_node.next = None
            next_node.data = None
        return head


node1 = ListNode(1)
node2 = ListNode(2,node1)
node3 = ListNode(3,node2)
node4 = ListNode(4,node3)

print(Solution.solve(node4,node2))
