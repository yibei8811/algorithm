from public.tree import Tree


class Solution:

    def __init__(self):
        self.find = False

    @staticmethod
    def solve(tree, k1, k2):
        vis1 = []
        vis2 = []
        Solution().dfs(tree, vis1, k1)
        Solution().dfs(tree, vis2, k2)
        for i in range(0, len(vis1)):
            if vis2[i] is None:
                return vis1[i-1]
            elif vis1[i] == vis2[i]:
                pass
            else:
                return vis1[i-1]

    def dfs(self, tree, vis, k):
        if tree is not None:
            vis.append(tree.val)
            if tree.val == k:
                self.find = True
            if self.find is not True:
                self.dfs(tree.left, vis, k)
            if self.find is not True:
                self.dfs(tree.right, vis, k)
            if self.find is not True:
                vis.pop(-1)
        if self.find is True:
            return vis
        return None


lst = ['1',
       '2', '3',
       '4', '5', '$', '6',
       '$', '$', '7', '$', '$', '$',
       '$', '$']
tree = Tree.deserialize_with_tail(lst)
print(Solution.solve(tree, '4', '7'))

