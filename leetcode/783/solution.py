class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.min

    def __init__(self):
        self.pre = None
        self.min = None

    def dfs(self, root):
        if root.left:
            self.dfs(root.left)
        if self.pre is not None and (self.min is None or root.val - self.pre < self.min):
            self.min = root.val - self.pre
        self.pre = root.val
        if root.right:
            self.dfs(root.right)

