class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self, data=None, next=None):
        return self.data


class Solution:
    @staticmethod
    def solve(var_node):
        if var_node.next is None:
            print(var_node)
        else:
            Solution.solve(var_node.next)
            print(var_node)

    @staticmethod
    def solve2(var_node):
        if var_node is None:
            return
        Solution.solve2(var_node.next)
        print(var_node)


node3 = Node('3')
node2 = Node('2',node3)
node1 = Node('1',node2)
Solution.solve(node1)
Solution.solve2(node1)
