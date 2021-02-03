from public.listnode import ListNode


class Solution:
    @staticmethod
    def solve(node1, node2):
        n1 = len(node1)
        n2 = len(node2)
        step = n1 - n2
        if step > 0:
            node = node1
            while step > 0:
                node = node.next_node
                step -= 1
        else:
            node = node2
            while step < 0:
                node = node.next_node
                step += 1
        return node


# 1.利用2个栈后进先出，从尾节点比较
# 2.判断lst，大小长度，长的先走n步
n1 = ListNode(1)
n2 = ListNode(2,n1)
n3 = ListNode(3,n2)
print(Solution.solve(n1, n2))
print(Solution.solve(n1, n3))
print(Solution.solve(n2, n3))
