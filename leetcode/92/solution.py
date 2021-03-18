class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        node = head
        stack = []
        start = None
        tail = None
        index = 1
        while node is not None:
            if index == left:
                while index != right:
                    stack.append(node)
                    node = node.next
                    index += 1
                stack.append(node)
                tail = node.next
                break
            else:
                start = node
                node = node.next
                index += 1
        while len(stack) > 0:
            stack_node = stack.pop(-1)
            if start is None:
                start = stack_node
                head = start
            else:
                start.next = stack_node
            start = stack_node
        start.next = tail
        return head

s = ListNode(5)
s1 = ListNode(3, s)
print(Solution().reverseBetween(s1, 1, 2))
