class Solution:
    @staticmethod
    def solve(tree):
        tmp = tree.left_node
        tree.left_node = tree.right_node
        tree.right_node = tmp
        if tree.left_node is not None:
            Solution.solve(tree.left_node)
        if tree.right_node is not None:
            Solution.solve(tree.right_node)


# TODO test
Solution.solve()
