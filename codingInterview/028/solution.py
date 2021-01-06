class Solution:
    @staticmethod
    def solve(tree):
        return Solution.diff(tree.left_node, tree.rigth_node)

    def diff(tree1, tree2):
        if tree1 is None and tree2 is None:
            return True
        if tree1 is None or tree2 is None:
            return False
        if tree1.data != tree2.data:
            return False
        return Solution.diff(tree1.left_node, tree2.right_node) and \
               Solution.diff(tree1.right_node, tree2.left_node)


# TODO test
Solution.solve()
