class Solution:
    @staticmethod
    def solve(tree, key, path):
        if tree is None:
            return
        path.append(tree.data)
        now = sum(_ for _ in path)
        if now == key:
            print(path)
            # return   # 找到是否继续搜索
        Solution.solve(tree.left_node, key, path)
        Solution.solve(tree.rigth_node, key, path)
        path.pop()


# TODO test
Solution.solve()
