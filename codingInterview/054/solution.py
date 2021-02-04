from public.tree import Tree


class Solution:
    @staticmethod
    def solve(tree, k):
        s = Solution(k)
        s.bfs(tree)
        return s.val

    def __init__(self, k=None, val=None):
        self.k = k
        self.val = val

    def bfs(self, tree):
        if tree is not None:
            self.bfs(tree.left)
            # 这样调用栈会更少 和 书中指针类似
            if self.val is None:
                self.k -= 1
                if self.k == 0:
                    self.val = tree.val
            # 这样调用栈会更少 和 书中指针类似
            if self.val is None:
                self.bfs(tree.right)


# 题目应该是第三小
lst = ['5', '3,', '7', '2', '4', '6', '8',
       '$', '$', '$', '$', '$', '$', '$', '$',
       '$', '$', '$', '$', '$', '$', '$', '$']
tree = Tree.deserialize_with_tail(lst)
print(Solution.solve(tree, 6))
