class Solution:
    @staticmethod
    def solve(tree):
        Solution.dfs(tree, None)

    def dfs(node, last_node):
        if node.left_node is not None:
            Solution.dfs(node.left_node, last_node)
        if last_node is not None:
            node.left_node = last_node
            last_node.right_node = node
        last_node = node
        if node.rigth_node is not None:
            Solution.dfs(node.right_node, last_node)


# TODO test
Solution.solve()
