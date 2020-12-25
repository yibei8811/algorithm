class Solution:
    @staticmethod
    def solve(node):
        if node.right_node is not None:
            return node.right_node
        else:
            node = Solution.solve_next(node)
            return node

    @staticmethod
    def solve_next(node):
        if node.up_node.right_node == node:
            return Solution.solve_next(node.up_node)
        else:
            return node.up_node


# Solution.solve(node)
# TODO test