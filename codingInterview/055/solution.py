from public.tree import Tree


class Solution:
    @staticmethod
    def solve(tree):
        if tree is not None:
            cur = 1
            next = 0
            result = 0
            queue = [tree]
            while len(queue) > 0:
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                    next += 1
                if node.right is not None:
                    queue.append(node.right)
                    next += 1
                cur -= 1
                if cur == 0:
                    cur = next
                    next = 0
                    result += 1
            return result
        return 0


lst = ['5', '3,', '7', '2', '4', '6', '8',
       '$', '$', '$', '$', '$', '$', '$', '$',
       '$', '$', '$', '$', '$', '$', '$', '$']
lst2 = ['1',
        '2,', '3',
        '4', '5', '$', '6',
        '$', '$', '7', '$', '$', '$',
        '$', '$']
tree = Tree.deserialize_with_tail(lst)
tree2 = Tree.deserialize_with_tail(lst2)
print(Solution.solve(tree))
print(Solution.solve(tree2))
