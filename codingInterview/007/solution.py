# 前序遍历：根结点 ---> 左子树 ---> 右子树
# 中序遍历：左子树---> 根结点 ---> 右子树
# 后序遍历：左子树 ---> 右子树 ---> 根结点
# 层次遍历：只需按层次遍历即可
# 前序 1,2,4,7,3,5,6,8
# 中序 4,7,2,1,5,3,8,6


class BinaryTreeNode:
    def __init__(self, data=None, left_node=None, right_node=None):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

    def __str__(self):
        return self.bfs()

    def bfs(self):
        result = []
        queue = [self]
        while len(queue) > 0:
            node = queue.pop(0)
            result.append(node.data)
            if node.left_node is not None:
                queue.append(node.left_node)
            if node.right_node is not None:
                queue.append(node.right_node)
        return result.__str__()


class Solution:
    @staticmethod
    def solve(pre_order, middle_order, node):
        root = pre_order[0]
        node.data = root
        root_index = middle_order.index(root)
        m_left = middle_order[0:root_index]
        m_right = middle_order[root_index+1:]
        p_left = pre_order[1:len(m_left)+1]
        p_right = pre_order[len(m_left)+1:]
        if len(m_left) > 0:
            node.left_node = BinaryTreeNode()
            Solution.solve(p_left, m_left, node.left_node)
        if len(m_right) > 0:
            node.right_node = BinaryTreeNode()
            Solution.solve(p_right, m_right, node.right_node)
        pass


node = BinaryTreeNode()
Solution.solve([1,2,4,7,3,5,6,8],
               [4,7,2,1,5,3,8,6],node)
print(node.bfs())
print(node)
