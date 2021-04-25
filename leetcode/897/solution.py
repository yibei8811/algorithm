# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.head = None
        self.pre = None
        self.dsf(root)
        return self.head

    def dsf(self, root):
        if not root:
            return
        self.dsf(root.left)
        if self.head == None:
            self.head = root
        if self.pre is not None:
            self.pre.right = root
        root.left = None
        self.pre = root
        self.dsf(root.right)

# 注意修改left = None
