class Solution:
    @staticmethod
    def bfs(tree):
        queue = [tree]
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.data)
            if node.left_node is not None:
                queue.append(node.left_node)
            if node.right_node is not None:
                queue.append(node.right_node)


# TODO test
