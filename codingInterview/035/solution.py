class Solution:
    @staticmethod
    def solve(lst):
        # head node
        node = {}
        Solution.bfs_copy(lst, node, dict)
        return node

    def bfs_copy(lst, node, dict):
        if dict[id(lst)] != 1:
            node.data = lst.data
            dict[id(lst)] = 1
            Solution.bfs_copy(lst.next, node.next, dict)
            Solution.bfs_copy(lst.sibling, node.sibling, dict)


# TODO test
Solution.solve()
