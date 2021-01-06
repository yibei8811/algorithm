class Solution:
    @staticmethod
    def solve(tree1, tree2):
        result = Solution.eq(tree1, tree2)
        if result is False:
            result = Solution.solve(tree1.left_node, tree2)
        if result is False:
            result = Solution.solve(tree1.right_node, tree2)
        return result

    @staticmethod
    def eq(tree1, tree2):
        if tree2.data is None:
            return True
        if tree1.data != tree2.data:
            return False
        return Solution.eq(tree1.left_node, tree2.left_node) \
               and Solution.eq(tree1.right_node, tree2.right_node)


# TODO test
Solution.solve()
